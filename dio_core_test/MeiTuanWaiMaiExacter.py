import mitmproxy
from mitmproxy import ctx

import pymongo
from dio_core.utils import json_util


injected_javascript = '''
Object.defineProperty(navigator, "languages", {
  get: function() {
    return ["zh-CN","zh","zh-TW","en-US","en"];
  }
});
Object.defineProperty(navigator, 'plugins', {
  get: () => [1, 2, 3, 4, 5],
});
Object.defineProperty(navigator, 'webdriver', {
  get: () => false,
});window.navigator.chrome = {
  runtime: {},
  // etc.
};const originalQuery = window.navigator.permissions.query;window.navigator.permissions.query = (parameters) => (
  parameters.name === 'notifications' ?
    Promise.resolve({ state: Notification.permission }) :
    originalQuery(parameters)
);
'''


class Cache(object):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client['dio']
    meituanwaimai_shop_list = db['meituanwaimai_shop_list_v1']
    meituanwaimai_food_list = db['meituanwaimai_food_list_v1']
    meituanwaimai_comment_list = db['meituanwaimai_comment_list_v1']


# 编码替换
def decryptCode(code):
    code.replace("&#xc80b;", "0").replace("&#xd11b;", "1").replace("&#xf0b5;", "2")\
        .replace("&#xb2e3;", "3").replace("&#x6267;", "5").replace("&#x7eca;", "6")\
        .replace("&#x3a90;", "7").replace("&#xe53a;", "8").replace("&#xe586;", "9")
    return code


def response(flow: mitmproxy.http.HTTPFlow):
    # Only process 200 responses of HTML content.
    if not flow.response.status_code == 200:
        return

    # webdriver 变量检测
    if "passport.csdn.net/login" in flow.request.url:
        html = flow.response.text
        html = html.replace('<title>', '<script>{}</script><title>'.format(injected_javascript))
        flow.response.text = str(html)
        ctx.log.info('>>>> js代码插入成功 <<<<')

    # 商店列表抓取
    if "i.waimai.meituan.com/openh5/homepage/poilist" in flow.request.url:
        html = flow.response.text
        data = json_util.to_python(html)
        for shop in data["data"]["shopList"]:
            try:
                shop["_id"] = shop["mtWmPoiId"]
                shop["shopName"] = decryptCode(shop["shopName"])
                shop["monthSalesTip"] = decryptCode(shop["monthSalesTip"])
                shop["deliveryTimeTip"] = decryptCode(shop["deliveryTimeTip"])
                shop["minPriceTip"] = decryptCode(shop["minPriceTip"])
                shop["shippingFeeTip"] = decryptCode(shop["shippingFeeTip"])
                shop["averagePriceTip"] = decryptCode(shop["averagePriceTip"])
                shop["distance"] = decryptCode(shop["distance"])
                shop["shipping_time"] = decryptCode(shop["shipping_time"])

                if "discounts2" in shop:
                    for discounts in shop["discounts2"]:
                        discounts["info"] = decryptCode(discounts["info"])
                Cache.meituanwaimai_shop_list.insert(shop)
            finally:
                pass
    #
    # # 商店信息抓取
    # if "http://i.waimai.meituan.com/openh5/poi/food" in flow.request.url:
    #     html = flow.response.text
    #     data = JsonUtil.to_python(html)
    #
    #     # for food in data["data"]["categoryList"]:
    #     #     shop["_id"] = shop["mtWmPoiId"]
    #     # Cache.meituanwaimai.update(shop)
    #
    #
    # # 评论列表抓取
    if "i.waimai.meituan.com/openh5/poi/comments" in flow.request.url:
        html = flow.response.text
        data = json_util.to_python(html)

        mtWmPoiId = data["data"]["mtWmPoiId"]
        for comment in data["data"]["list"]:
            comment["mtWmPoiId"] = mtWmPoiId

        Cache.meituanwaimai_comment_list.insert_many(data["data"]["list"])
