import collections
import functools
import json
import logging
import time
import traceback
import uuid
from urllib import parse

import requests

from DioCore.Utils import random_utils, ThreadUtil


logging.basicConfig(level=logging.INFO, filemode='w',
                    format="[%(asctime)s]-[%(name)s]-[%(levelname)s]-[%(thread)d:%(threadName)s]: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename="test.{}.log".format(uuid.uuid4()))

console_handler = logging.StreamHandler()

def get_host():
    host_list = [
        "vp-orayshb-026.oicp.vip",
        "vp-orayshb-026.ticp.net"
    ]
    return random_utils.get_random_ele_form_list(host_list)

to_json = functools.partial(json.dumps, separators=(',', ':'), ensure_ascii=False)


x_t = int(round(time.time()))
lat, lng = random_utils.get_random_location()
utdid = random_utils.get_random_string(24)
umt = random_utils.get_random_string(32)
devid = random_utils.get_random_string(44)

exParams = collections.OrderedDict({
    "action": "ipv",
    "countryCode": "CN",
    "cpuCore": "4",
    "cpuMaxHz": "2265600",
    "from": "search",
    "id": "1231231231231",
    "item_id": "1231231231231",
    "latitude": str(lat),
    "list_type": "search",
    "longitude": str(lng),
    "osVersion": "23",
    "phoneType": "Nexus 5",
    "search_action": "initiative",
    "soVersion": "2.0",
    "utdid": utdid
})

data = collections.OrderedDict({
    "detail_v": "3.1.1",
    "exParams": to_json(exParams),
    "itemNumId": "1231231231231"
})

params = collections.OrderedDict({
    "deviceId": devid,
    "appKey": "21646297",
    "api": "mtop.taobao.detail.getdetail",
    "data": to_json(data),
    "utdid": utdid,
    "x-features": "27",
    "ttid": "703304@taobao_android_7.6.0",
    "lng": str(lng),
    "v": "6.0",
    "sid": None,
    "t": x_t,
    "uid": None,
    "lat": str(lat),
})
data_ = parse.quote(to_json(params))


# sign 获取 retry
def get_sign(i):

    while True:
        sign = None
        i = 0
        while i < 3:
            host = get_host()
            try:
                start = time.time()
                logging.info("【接口: {}】尝试获取 sign , ".format(host))
                sign = requests.get("http://{}/?data={}".format(host, data_)).json()["data"]
                logging.info("【接口: {}】获取sign success {} {:.3f}".format(host, sign, time.time() - start))
                break
            except Exception as e:
                logging.error("【接口:{}】获取sign fail {}".format(host, str(e)))
                logging.error("【接口:{}】打印异常栈: {}".format(host, traceback.format_exc()))
            finally:
                i += 1

        if sign is None:
            logging.error("连续3次获取sign 失败")


ThreadUtil.multiThreadRun(get_sign, 10)
