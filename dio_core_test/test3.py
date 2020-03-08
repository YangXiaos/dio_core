import collections
import traceback

from dio_core.network.downloader import Downloader, Setting
from dio_core.utils import thread_util, time_util, json_util, url_util, random_util
from dio_core.utils.file_util import csv_util

thread_num = 30


rows = csv_util.get_rows_from_csv("/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/item_id.csv")[1:]

def getSign(i):
    while True:

        x_t = time_util.get_unix_v2()
        HOST = "192.168.1.103"
        row = random_util.get_random_ele_from_list(rows)

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
            "exParams": json_util.to_json(exParams),
            "itemNumId": row[0]
        })


        params = collections.OrderedDict({
            "deviceId": "AuI9v8NvMf8kPEACBJUBffn0N6wOeMTO1lYOHPKDqOvh",
            "appKey": "21646297",
            "api": "mtop.taobao.detail.getdetail",
            "data": json_util.to_json(data),
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
            data_ = url_util.quote(json_util.to_json(params))
            sign = Downloader(setting=Setting()).get("http://{}/?data={}".format(HOST, data_)).json()["data"]
            print("{}号线程 测试 itemId[{}] [{}]".format(i, row[0], sign))
            time_util.sleep(3)
        except Exception as e:
            traceback.print_exc()
            print("请求异常 {}".format(e))


thread_util.multi_thread_run(getSign, 40)