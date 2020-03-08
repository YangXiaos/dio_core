import jsonpath

from dio_core.network.downloader import Downloader
from dio_core.utils import json_util, url_util, time_util
from dio_core_test.utils import text_util

keyword = "女装"


for i in range(100):
    html = Downloader.get("https://shopsearch.taobao.com/browse/shop_search.htm?q={}&s={}".format(keyword, i * 20)).text
    data = json_util.to_python(text_util.get_first_match(html, "g_page_config = (.*);"))
    for shop in jsonpath.jsonpath(data, "$.mods.shoplist.data.shopItems.*"):
        if "shopIcon" in shop and "title" in shop["shopIcon"] and "天猫" in shop["shopIcon"]["title"]:
            print("天猫\t{}\t{}".format(url_util.patch_url(shop["shopUrl"]), shop["procnt"]))
        else:
            print("淘宝\t{}\t{}".format(url_util.patch_url(shop["shopUrl"]), shop["procnt"]))
    time_util.sleep(5)