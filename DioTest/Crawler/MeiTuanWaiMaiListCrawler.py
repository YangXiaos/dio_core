import traceback

import pymongo

from DioCore.Network.Downloader import Downloader
from DioCore.Network.Downloader.Downloader import Setting
from DioCore.Utils import LoggerUtil, TimeUtil, Md5Util, UrlUtil
from DioCore.Utils.FileUtil import CSVUtil

logger = LoggerUtil.getLogger(__file__)

fields = ("_id,productList,name,monthSalesTip,wmPoiScore,distance,shippingFeeTip,minPriceTip,deliveryTimeTip,averagePri"
          "ceTip,thirdCategory,recommendInfo,activityList,labelInfoList,keyword,url")


# 主页url, 搜索url,
MAIN_URL = "http://h5.waimai.meituan.com/waimai/mindex/home"
SEARCH_URL = "http://i.waimai.meituan.com/openh5/search/poi"
SHOP_SEARCH_URL = "http://i.waimai.meituan.com/openh5/homepage/poilist?_={}"
FOOD_URL = "http://i.waimai.meituan.com/openh5/poi/food"
COMMENT_URL = "http://i.waimai.meituan.com/openh5/poi/comments"


# mongodb 配置
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['meituan']
meituanwaimai_shop_list = db['meituanwaimai_shop_list_v1']
meituanwaimai_search_list = db['meituanwaimai_search_list']
meituanwaimai_food_list = db['meituanwaimai_food_list_v1']
meituanwaimai_comment_list = db['meituanwaimai_comment_list_v1']
decrypt_collection = db["meituanwaimai_decrypt"]


decrypt = decrypt_collection.find_one({"_id": 1})["match"]


setting = Setting()
setting.headers = {
    "Origin": "http://h5.waimai.meituan.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
    "Referer": "http://h5.waimai.meituan.com/waimai/mindex/home",
    "Host": "i.waimai.meituan.com",
    # "Cookie": '_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16cae674b36c8-01bf1cb1fd7b27-29792349-5df1a-16cae674b36c8; _ga=GA1.3.2021950140.1566294101; _gid=GA1.3.138356466.1566294101; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=23UFuT0gtxcARBkc-Il6MOl2sihlNPJY7at6eTLmNTIUTgjS2XMaI4KAEWZGc_jm; utm_source=0; wx_channel_id=0; JSESSIONID=ok0xdngf40ahhx0dbvhg0atd; webp=1; __mta=45921691.1566294104072.1566294104072.1566294104072.1; w_addr=; w_actual_lat=23124630; w_actual_lng=113361990; wm_order_channel=default; utm_source=; au_trace_key_net=default; iuuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; token=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; mt_c_token=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; oops=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; userId=64012031; cssVersion=e09c1174; _lxsdk=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; openh5_uuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; uuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; w_token=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; openh5_uuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C,_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16cae674b36c8-01bf1cb1fd7b27-29792349-5df1a-16cae674b36c8; _ga=GA1.3.2021950140.1566294101; _gid=GA1.3.138356466.1566294101; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; w_uuid=23UFuT0gtxcARBkc-Il6MOl2sihlNPJY7at6eTLmNTIUTgjS2XMaI4KAEWZGc_jm; utm_source=0; wx_channel_id=0; JSESSIONID=ok0xdngf40ahhx0dbvhg0atd; webp=1; __mta=45921691.1566294104072.1566294104072.1566294104072.1; w_addr=; w_actual_lat=23124630; w_actual_lng=113361990; wm_order_channel=default; utm_source=; au_trace_key_net=default; iuuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; token=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; mt_c_token=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; oops=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; userId=64012031; cssVersion=e09c1174; _lxsdk=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; openh5_uuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; uuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; w_token=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; openh5_uuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; uuid=86f1d5d1-b229-4c12-a7bd-10dc5ef16e45; terminal=i; w_utmz="utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)"; utm_source=; au_trace_key_net=default; wm_order_channel=default; _lx_utm=utm_source%3D60066; cssVersion=d70fc3f0; w_actual_lat=23125752; w_actual_lng=113334715; w_latlng=0,0; w_token=yDDjkm8ceYOgcuQ4qyaFMy3swNQAAAAA5wgAAHkBWapv9B8SL5PDs_OYrNT8vbNXv7Ua7Ty5u_9n3opjKT5T8ZXLpsrAm3n9Xf-cIg; openh5_uuid=EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C; w_visitid=58b6dcfb-0534-4b2a-9faa-a6f00f06d908',
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


post_data_of_food_list = {
    "geoType": "2",
    "mtWmPoiId": "1019849762432818",
    "dpShopId": "-1",
    "source": "shoplist",
    "skuId": "",
    "uuid": "2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340",
    "platform": "3",
    "partner": "4",
    "originUrl": "http://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId=1019849762432818&utm_source=&source=shoplist&initialLat=&initialLng=&actualLat=23.125752&actualLng=113.334715",
    "riskLevel": "71",
    "optimusCode": "10",
    "wm_latitude": "0",
    "wm_longitude": "0",
    "wm_actual_latitude": "23125752",
    "wm_actual_longitude": "113334715",
    "openh5_uuid": "2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340",
    "_token": "eJxVkG2PmkAUhf8LH/yigWFgAE1MgysoLqyCL7A2TYO8yAgzIi+KNv3vnW3dNk0mOec+9yRzcn9wlRVzIxGIKhAH3DWpuBEn8oBXuAHX1GyDFAVqiqKJiiIPuOg/BjWgDrhDtZtyo68yUgeaDL99AI/N/8A/B2X2PhIWC3BZ05QjQcgQfwsxCTFPEty0IeWjMxH+IIFgGiedQBLafonLdXYurXjcI83TseJDTR6qCpQlqIlar23I9/rcVlEy7j21ZtEC100PU9zgsLDDZvzX0+O4F0bs198YSrwIkYrgJ2NrUZR4SZJVEbGTcKw82bDyTPOnhk9tPmeH3ZBla3ykzCWLe5Obw9Xtrm+7g2DPKX7Yu4kf5rYDy8DY6xoJaVffrXPjp2Rjll0/kWYV0LpgfjtKSHy0/cAMaFBHlX29Qh0Y14O3mgP5PrE9AbhD3/MKUr96yA8775TNTNM80sd2GhrmZr5dOKeTOTedWDhO8GIZFupjs8uhtyvW67KRNTvE5XJmnfWSxO6uDC63DA3rVyTmESq3ywgCdbZf6nS3vj5WDqhrU41RS3RAli4hmYHhbqpZeaJcNzXyLvtNhSgpy1sjFbPOHF5SxZ0owgG+70u7K97VE4EnUkF3QovCy6Rb9WYfgvOsmyqEkrVhyJnlxi+SSYAVvS+6INdf6AJrubeyj15rpqq/2WeZE57UGi3qyHfnk1TP0vQtXQjqyjpDdeXPROeE2tc+8GQ5lQo/XqaPLe4fjVTSWhcgJSp9Cby8XeBF08dj7ucvTzvzJg==",
}

shop_list = set()

# 获取ttf url
# res = Downloader.get(MAIN_URL, setting=setting)
# ttfUrl = "http://"+ TextUtil.getFirstMatch(res.text, "format\(\"embedded-opentype\"\),url\(\"//(.*?\.woff)\"\)")
# fileName = ttfUrl.split("/")[-1]
# logger.info("抽取ttf {}".format(ttfUrl))

# 获取ttf 文件
# res = Downloader.get(ttfUrl)
# with open(fileName, "wb") as file:
#     file.write(res.content)

# ttf 文件解析
# font = TTFont(fileName)
# font.get("glyf")
# font.getTableData("glyf")
#
# for key in font["glyf"].glyphs:
#     f = font["glyf"].glyphs[key]
#     if not hasattr(f, "flags"):
#         continue
#     if str(f.flags.tolist()) in ttfMatch:
#         decrypt[key.lower().replace("uni", "&#x") + ";"] = ttfMatch[str(f.flags.tolist())]
# decrypt_collection.save({"_id": 1, "match": decrypt})


# ttf 解析
def ttfDecrypt(obj):
    if isinstance(obj, str):
        for key, val in decrypt.items():
            obj = obj.replace(key, str(val))
        return obj
    elif isinstance(obj, list):
        for ind in range(len(obj)):
            obj[ind] = ttfDecrypt(obj[ind])
        return obj
    elif isinstance(obj, dict):
        for key, val in obj.items():
            obj[key] = ttfDecrypt(val)
        return obj
    else:
        return obj


# 抓取商店列表
setting.headers.update({
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json",
})


# 商品搜索
def searchShopList(keyword: str, latitude: str, longitude: str, topN: int=1000):
    post_data = ("geoType=2&cityId=1&secondCategoryId=&start=0&queryType=12002&keyword=%E7%B2%A5&categoryType=&entrance"
                 "Id=0&uuid=16cb375798ab8-07b01f3c8b2835-1a201708-1fa400-16cb375798bc8&platform=3&partner=4&originUrl=h"
                 "ttp%3A%2F%2Fh5.waimai.meituan.com%2Fwaimai%2Fmindex%2Fsearchresults%3FqueryType%3D12002%26keyword%3D%"
                 "25E7%25B2%25A5%26entranceId%3D0%26qwTypeId%3D0%26mode%3Dsearch&riskLevel=71&optimusCode=10&wm_latitud"
                 "e=23125801&wm_longitude=113334718&wm_actual_latitude=23125801&wm_actual_longitude=113334718&openh5_uu"
                 "id=16cb375798ab8-07b01f3c8b2835-1a201708-1fa400-16cb375798bc8&_token=eJxVUNmOolAQ%2FReS7heNcEEWTcyETT"
                 "bBVhHByTwgXBZZxMsmdubfh57uSWeSSs5SJ5WqeseQFmJLQACWAFOsgwhbYmBGzBhsijX12KEZhmIXAAAWEFMs%2BM8jAcFNsQtyJ"
                 "Gz5kwZgys3JXx%2FGftTfxjcj52N9JLQxgCVNUy1xPKFnvZ8WfjorYNq0fjkLbgX%2BaeFFWobwgdfQR0GCYN3mTf3j3kI02EMFV4"
                 "AkCPI1g0N%2FQ%2BHqRWZfBPKFp19h2SC%2FDKAWrojXe%2F%2BR%2FUuLWwhXn8PGA7FxlcIeVxkx%2B0L%2FC5t%2F2hw%2FMmb"
                 "rNC5HBvUhP8rNtn%2Fyx05uc1hFSjn3PJ1vhMfO0HW%2FRw8qt5B5Jv1rK6tavAnEoo2jdi%2FmDsW%2B9ZzKUaZtZto1erOZxUHa"
                 "yUhlLtlJ0BTLzW9rJhBvvAt5I0SiJVVROpl09mTP1Ar5UGM%2FFCR49wpnT5X6mdsN7vrgXaoyWW8P9aClWaFD70wGcf5oirMrFvB"
                 "iaOQOpLQS28KglqH%2F1hXbhaqQFp5Dp67398ICfC1tY%2FawqXbPSSQja4FOnC6r2ZoBar3ZPVwRVybSMQGi%2BWTU0p64XBbMox"
                 "ThTdhuIaRSP%2FLSqwLv%2BfXhcyfDmGSUeu0E2XSdilUvXsfxTGjwmXHTh8ZhQiEbZMM8ZxmFL1pLvwPHyNmGoPdEHFf66SSvk8G"
                 "m6PT53MtZIinkxswF6DhDYncsf3QLJPQr7Pcfj3reuA%3D%3D")
    data = UrlUtil.unquotePostData(post_data)
    data["keyword"] = keyword
    data["start"] = "0"
    data["wm_latitude"] = latitude
    data["wm_longitude"] = longitude
    data["wm_actual_latitude"] = latitude
    data["wm_actual_longitude"] = longitude

    fieldList = fields.split(",")
    CSVUtil.save2csvV3("poi.csv", fieldList)
    total = 0
    while True:
        jsonObject = None
        try:
            # 请求解析
            res = Downloader(setting).post(SEARCH_URL, data)
            jsonObject = res.json()
            logger.info("{} 抓取第{}页 数量：{}".format(keyword, data["start"], len(jsonObject["data"]["searchPoiList"])))

            # 抽取数据
            total += len(jsonObject["data"]["searchPoiList"])
            ttfDecrypt(jsonObject["data"]["searchPoiList"])
            for poi in jsonObject["data"]["searchPoiList"]:
                poi["_id"] = poi["id"]
                poi["keyword"] = keyword
                poi["url"] = "http://h5.waimai.meituan.com/waimai/mindex/menu?mtShopId={}".format(poi["_id"])
                CSVUtil.save2csvV3("poi.csv", poi, fieldList)

            # 判断是否翻页
            if not jsonObject["data"]["hasNextPage"] or total > topN:
                logger.info("抓取第{}页 总数量{}".format(data["start"], total))
                logger.info("翻页抓取结束")
                break
            data["start"] = str(int(data["start"]) + 1)

        except Exception as e:
            traceback.print_exc()
            data["start"] = str(int(data["start"]) + 1)
            logger.error("{}页抓取异常，jsonObject: {}".format(data["start"], jsonObject))


# 抓取商店列表
def crawlShopList():
    post_data_of_shop_list = {
        "startIndex": "0",
        "sortId": "0",
        "multiFilterIds": "",
        "sliderSelectCode": "",
        "sliderSelectMin": "",
        "sliderSelectMax": "",
        "geoType": "2",
        "rankTraceId": "",
        "uuid": "EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C",
        "platform": "3",
        "partner": "4",
        "originUrl": "http://h5.waimai.meituan.com/waimai/mindex/home",
        "riskLevel": "71",
        "optimusCode": "10",
        "wm_latitude": "23129112",
        "wm_longitude": "113264385",
        "wm_actual_latitude": "",
        "wm_actual_longitude": "",
        "openh5_uuid": "EDAF663058DC10DD9DA74BF73550627E0BA82B4963E47B9FAEA941817D9F2F1C",
        "_token": ("eJx9kG2PmkAUhf/LJNsvEgcFBExMI7CyuAgi43SlaRoEVORtweFFmv73DjHN7oemyU3uuc+9J3Myv0BlhGA+YSciO2FAE1VgDiZ"
                   "jdjwDDCA3uhFms6nMT1lR5KYMCD6ziShLPAOOFdbA/DsviIzET38MYEfnD/Chpjyt4cKgB+BCyPscwoswbv048+NxFsWk9vNxUG"
                   "TwgWAW52HUDS2iif7rSItznH89FVUQLUhVR1+OfpD8rKt0MdieuOXTdEXrn2bKH5CKx5MPEQGaNkNDWklmRFkY5mSYafc/cUYz8"
                   "LAjf3cb+pE08S0+51RF6ztJNNKc+6XTibKpFPBy9XVXkZZn44gR26VeYGAEnzXdsjOukje2j965xhqFsJDEXlfs/F632esltOvO"
                   "sStNJtoqxkQxrboVUdmn2DvlrnfGjZGqfUIi9ohqf71ODzsRWeW9MkoRbRLop5aXYhHjbO+tdi+512FuH2n6i08kf9PqppMZt76"
                   "8nirdNYMRQc9q70nu2lFRWzpmYJ52d0vNBadYKdtgyX4rePXWXgsrLXGSBq+yPiMHp+wdQdhgAzrI6HxO6i3prDus8d48q1Fbuc"
                   "o1JDDRot3L27ZVJ4p0mJmd6/ZvWQ/rI7lAKLTs3jo0SBZsDY1mr9zOHB3Y0ybcpn2A+aDZh/YWLxcL8PsPSaDfFA=="),
    }

    total = 0
    while True:
        # download 解析
        res = Downloader.post(SHOP_SEARCH_URL.format(TimeUtil.getUnix()), post_data_of_shop_list, setting=setting)
        jsonObject = res.json()

        # 判断是否请求结束
        if total > 2000:
            logger.info("商品列表超过两千，结束请求")
            break

        # 判断是否请求异常
        if "data" not in jsonObject or not isinstance(jsonObject["data"], dict):
            logger.error("第[{}]次 登录失效 or 接口异常 ".format(post_data_of_shop_list["startIndex"]))
            post_data_of_shop_list["startIndex"] = str(int(post_data_of_shop_list["startIndex"]) + 1)
            continue

        # 解析抽取
        try:
            for shop in jsonObject["data"]["shopList"]:
                shop["_id"] = shop["mtWmPoiId"]
                ttfDecrypt(shop)
                meituanwaimai_shop_list.save(shop)
                shop_list.add(shop["mtWmPoiId"])
            total += len(jsonObject["data"]["shopList"])

            # 写入数据库
            logger.info("第[{}]次 请求，抓取数据 {}量".format(post_data_of_shop_list["startIndex"], len(jsonObject["data"]["shopList"])))
        except Exception as e:

            #
            logger.error("第[{}]次 解析失败 或 插入失败".format(post_data_of_shop_list["startIndex"]))
            traceback.print_exc()

        post_data_of_shop_list["startIndex"] = str(int(post_data_of_shop_list["startIndex"]) + 1)
        TimeUtil.sleep(5)


# 抓取餐品清单
def crawlFoodMenus(shopId: str):
    logger.info("抓取 餐品清单 {}".format(shopId))
    post_data_of_food_list["mtWmPoiId"] = shopId
    res = Downloader(setting=setting).post(FOOD_URL, post_data_of_food_list)
    jsonObject = res.json()

    try:
        categoryList = jsonObject["data"]["categoryList"]
        ttfDecrypt(categoryList)

        # 抓取餐品id
        for category in categoryList:
            for spu in category["spuList"]:
                spu["_id"] = "{}_{}_{}".format(category["tag"], shopId, spu["spuId"])
                spu["mtWmPoiId"] = shopId
                spu["categoryName"] = category["categoryName"]
                meituanwaimai_food_list.save(spu)
    except Exception as e:
        traceback.print_exc()


# 抓商品评论
def crawlComment(shopId: str):
    post_data_of_comment_list = "lng=113.334699&lat=23.125753&gpsLng=113.334699&gpsLat=23.125753&shopId=0&mtWmPoiId=1113200877771207&startIndex=0&labelId=0&scoreType=0&uuid=16d0af3bce3c8-0b9b6f8144bd7e-29792349-6b82e-16d0af3bce4c8&platform=3&partner=4&originUrl=https%3A%2F%2Fh5.waimai.meituan.com%2Fwaimai%2Fmindex%2Fmenu%3FdpShopId%3D%26mtShopId%3D1113200877771207%26utm_source%3D%26source%3Dshoplist%26initialLat%3D%26initialLng%3D%26actualLat%3D23.125753%26actualLng%3D113.334699&riskLevel=71&optimusCode=10&wm_latitude=0&wm_longitude=0&wm_actual_latitude=23125753&wm_actual_longitude=113334699&openh5_uuid=16d0af3bce3c8-0b9b6f8144bd7e-29792349-6b82e-16d0af3bce4c8&_token=eJyVkWuPmkAUhv8LH%2FyiEYZBBkxMgxeUy64CgrJN04CAIAy4MOBi0%2F%2Fesd3t9msnk5x3nvck5zI%2FmFqLmCngAOLAiOnimpkyYMyNRWbEkIY6ExFJAgIAiUgYMad%2FGc9JgjhiwtpbMtOvEx6OJIH%2F9gA2fX%2BCT8UL9D4yNJrApIRcmynLppPxLchwkI1xnJE2KMenCrN%2FEIuzMorfWByX7Zfo6qTVVYtmA0zeFQAA8hwnIXpoQ2jQEvy9qdr6FM8G77GhqUXWkEFWZiQLCjMgs7%2B6PM8GwYlW%2FY15OAb8BE3gB6M2rTCGUBBlme7kf3pOKxwzdFq8f0zLi2hEt%2FgA%2BQPQGPxrjJaa9zDJh%2FlEv4JWbLJzSVWs90Vuku3trrgpGao3r3GOUFebNPON0lOUxva3Pg4PuzPmxc1NvvbOq2lnutbu7mxBErZs9ZSFWrkxTrlRX7FZQVPZ68K%2BuOgeAP2KxK8F1KTIOjoJCE99%2FszuclWx9GhRrkPrKanCdH7PG%2BQJUeHuF43d99t6LuVruXqSAUg2gDhFB%2F1ee%2BP3bvTCHzwAgfHCHkKz8r0wv%2BhmsnEuE8W6qLKTo3VnJSukv7Ftho1O0nXLNi6Rc3WPfrJZ4IPaqu4xcEvhYEdl7rPJrtnpykJWQ9n3RGfrOjBdqT0xOLsqajXVbc%2BxClkt46tl%2BY6C%2BtcQgrbzyPFY2flLrBRSu%2BREzUyXiutBNuktvo5Xc2ujDvdmMYnPu0DU3IUlkHvHzvn7MEie82XWBbRlRc2zIlxvh%2FiSo9rdnuFwnsYXvEhgcFyZCM2JZ3Tb84z5%2BQvKAQ0P"

    logger.info("抓取 餐品评论 {}".format(shopId))
    res = Downloader(setting=setting).payload(COMMENT_URL, post_data_of_comment_list)
    jsonObject = res.json()

    try:
        for comment in jsonObject["data"]["list"]:
            comment["mtWmPoiId"] = shopId
            md5 = Md5Util.md5("_".join([comment["commentTime"], comment["content"], str(comment["score"]), comment["deliveryTime"]]))
            comment["_id"] = "_".join([str(comment["userID"]), shopId, md5])
            meituanwaimai_comment_list.save(comment)
    except:
        pass


if __name__ == '__main__':
    searchShopList("coco", "23125801", "113334718")
    # crawlComment("10552832437354761055283243735476")
    # crawlFoodMenus("10552832437354761055283243735476")
