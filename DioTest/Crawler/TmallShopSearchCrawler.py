import jsonpath

from DioCore.Network.Downloader import Downloader
from DioCore.Utils import TextUtil, JsonUtil, UrlUtil, TimeUtil

keyword = "女装"


for i in range(100):
    html = Downloader.get("https://shopsearch.taobao.com/browse/shop_search.htm?q={}&s={}".format(keyword, i * 20)).text
    data = JsonUtil.toPython(TextUtil.getFirstMatch(html, "g_page_config = (.*);"))
    for shop in jsonpath.jsonpath(data, "$.mods.shoplist.data.shopItems.*"):
        if "shopIcon" in shop and "title" in shop["shopIcon"] and "天猫" in shop["shopIcon"]["title"]:
            print("天猫\t{}\t{}".format(UrlUtil.patchUrl(shop["shopUrl"]), shop["procnt"]))
        else:
            print("淘宝\t{}\t{}".format(UrlUtil.patchUrl(shop["shopUrl"]), shop["procnt"]))
    TimeUtil.sleep(5)