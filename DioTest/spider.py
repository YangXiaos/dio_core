# @Time         : 19-9-10 下午1:56
# @Author       : DioMryang
# @File         : test.py
# @Description  : 淘宝爬虫测试
import collections
import functools
import json
import random
import string
import time
from urllib import parse

import requests


PROXY_URL = ("http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1"
             "&sb=0&pb=45&mr=1&regions=")
PROXY_COUNT = collections.defaultdict(int)

PROXY = {
    'http': 'http://H4936U3JQF9UU61D:96F1A8624A4D9AB9@http-dyn.abuyun.com:9020',
    'https': 'http://H4936U3JQF9UU61D:96F1A8624A4D9AB9@http-dyn.abuyun.com:9020'
}

results = []
with open("./ids_5_1", "r") as file:
    for line in file.readlines():
        line = line.strip('\n')
        results.append(line.replace('"', ''))


# 获取随机字符串
def getRandomString(num: int) -> str:
    return "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase, num))


# json 转码工具函数
toJson = functools.partial(json.dumps, separators=(',', ':'), ensure_ascii=False)

HOST = "2ek6836376.wicp.vip"

i = 0
while True:
    try:

        item_id = random.choice(results)

        x_t = int(round(time.time()))
        utdid = "XW/eOqol6igDAO6KQj0b4Q3e"

        exParams = collections.OrderedDict({
            "action": "ipv",
            "countryCode": "CN",
            "cpuCore": "4",
            "cpuMaxHz": "2265600",
            "from": "search",
            "id": item_id,
            "item_id": item_id,
            "latitude": "23.125712",
            "list_type": "search",
            "longitude": "113.334662",
            "osVersion": "23",
            "phoneType": "Nexus 5",
            "search_action": "initiative",
            "soVersion": "2.0",
            "utdid": utdid
        })

        data = collections.OrderedDict({
            "detail_v": "3.1.1",
            "exParams": toJson(exParams),
            "itemNumId": item_id
        })

        params = collections.OrderedDict({
            "deviceId": "AuI9v8NvMf8kPEACBJUBffn0N6wOeMTO1lYOHPKDqOvh",
            "appKey": "21646297",
            "api": "mtop.taobao.detail.getdetail",
            "data": toJson(data),
            "utdid": utdid,
            "x-features": "27",
            "ttid": "703304@taobao_android_7.6.0",
            "lng": "113.334662",
            "v": "6.0",
            "sid": None,
            "t": x_t,
            "uid": None,
            "lat": "23.125712",
        })

        print("尝试获取 sign")
        start = time.time()
        data_ = parse.quote(toJson(params))
        sign = requests.get("http://{}/?data={}".format(HOST, data_), timeout=30).json()["data"]
        end = time.time()
        print("获取 sign success {} 耗时{:.3f}s".format(sign, end - start))

        headers = {}
        headers["x-features"] = "27"
        headers["x-location"] = "113.334662%2C23.125712"
        headers["user-agent"] = "MTOPSDK%2F3.0.4.7+%28Android%3B6.0.1%3BLGE%3BNexus+5%29"
        headers["x-ttid"] = "703304%40taobao_android_7.6.0"
        headers["cache-control"] = "no-cache"
        headers[
            "a-orange-q"] = "appKey=21646297&appVersion=7.6.0&clientAppIndexVersion=1120190910120003337&clientVersionIndexVersion=1220190910120003337"
        headers["x-appkey"] = "21646297"
        headers["x-nq"] = "WIFI"
        headers["content-type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        headers["x-pv"] = "5.1"
        headers["x-t"] = "{}".format(x_t)
        headers["x-app-ver"] = "7.6.0"
        headers["f-refer"] = "mtop"
        headers["x-nettype"] = "WIFI"
        headers["x-utdid"] = "XW%2FeOqol6igDAO6KQj0b4Q3e"
        headers["x-umt"] = "nlZLqC5LOv1GiDVtFdgIWjxpCFf0Y5w5"
        headers["x-devid"] = "AuI9v8NvMf8kPEACBJUBffn0N6wOeMTO1lYOHPKDqOvh"
        headers["x-sign"] = sign
        headers["Host"] = "trade-acs.m.taobao.com"
        headers["Accept-Encoding"] = "gzip"
        headers["Connection"] = "Keep-Alive"

        start = time.time()
        print(requests.get(
            "http://trade-acs.m.taobao.com/gw/mtop.taobao.detail.getdetail/6.0/?data={}".format(parse.quote(toJson(data))),
            headers=headers, timeout=5, proxies=PROXY).text)
        i += 1
        end = time.time()
        print("获取 res success {} 耗时{:.3f}s".format(sign, end - start))
        print("{} 第{} 次 采集成功".format(item_id, i))
    except Exception as e:
        print(e)
