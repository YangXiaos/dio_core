import collections
import traceback

from DioCore.Network.Downloader import Downloader, Setting
from DioCore.Utils import ThreadUtil, TimeUtil, RandomUtil, JsonUtil, UrlUtil
from DioCore.Utils.FileUtil import CSVUtil

thread_num = 30


rows = CSVUtil.getRowsFromCsv("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/item_id.csv")[1:]

def getSign(i):
    while True:

        x_t = TimeUtil.getUnixV2()
        HOST = "192.168.1.103"
        row = RandomUtil.getRandomEleFromList(rows)

        exParams = collections.OrderedDict({
            "action": "ipv",
            "countryCode": "CN",
            "cpuCore": "4",
            "cpuMaxHz": "2265600",
            "from": "search",
            "id": row[0],
            "item_id": row[0],
            "latitude":"23.125712",
            "list_type": "search",
            "longitude":"113.334662",
            "osVersion":"23",
            "phoneType":"Nexus 5",
            "search_action":"initiative",
            "soVersion":"2.0",
            "utdid":"XW/eOqol6igDAO6KQj0b4Q3e"
        })

        data = collections.OrderedDict({
            "detail_v": "3.1.1",
            "exParams": JsonUtil.toJson(exParams),
            "itemNumId": row[0]
        })


        params = collections.OrderedDict({
            "deviceId": "AuI9v8NvMf8kPEACBJUBffn0N6wOeMTO1lYOHPKDqOvh",
            "appKey": "21646297",
            "api": "mtop.taobao.detail.getdetail",
            "data": JsonUtil.toJson(data),
            "utdid": "XW/eOqol6igDAO6KQj0b4Q3e",
            "x-features": "27",
            "ttid": "703304@taobao_android_7.6.0",
            "lng": "113.334662",
            "v": "6.0",
            "sid": None,
            "t": x_t,
            "uid": None,
            "lat": "23.125712",
        })
        try:
            data_ = UrlUtil.quote(JsonUtil.toJson(params))
            sign = Downloader(setting=Setting()).get("http://{}/?data={}".format(HOST, data_)).json()["data"]
            print("{}号线程 测试 itemId[{}] [{}]".format(i, row[0], sign))
            TimeUtil.sleep(3)
        except Exception as e:
            traceback.print_exc()
            print("请求异常 {}".format(e))


ThreadUtil.multiThreadRun(getSign, 40)