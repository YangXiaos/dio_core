import collections

from DioCore.Utils import JsonUtil, UrlUtil


params = collections.OrderedDict({
    "deviceId": "AuI9v8NvMf8kPEcaBJUBffn0N6wOeMTO1lYOHPKDqOvh",
    "appKey": "21646297",
    "api": "mtop.taobao.detail.getdetail",
    "data": JsonUtil.toJson(collections.OrderedDict({
        "detail_v":"3.1.1",
        "exParams":"{\"action\":\"ipv\",\"countryCode\":\"CN\",\"cpuCore\":\"4\",\"cpuMaxHz\":\"2265600\",\"from\":\"search\",\"id\":\"570083263564\",\"item_id\":\"570083263564\",\"latitude\":\"23.125712\",\"list_type\":\"search\",\"longitude\":\"113.334662\",\"osVersion\":\"23\",\"phoneType\":\"Nexus 5\",\"search_action\":\"initiative\",\"soVersion\":\"2.0\",\"utdid\":\"XW/eOqol6igDAO6KQj0b4Q3e\"}",
        "itemNumId":"570083263564"
    })),
    "utdid": "XW/eOqol6igDAO6KQj0b4Q3e",
    "x-features": "27",
    "ttid": "703304@taobao_android_7.6.0",
    "lng": "113.334662",
    "v": "6.0",
    "sid": None,
    "t": "1568090463",
    "uid": None,
    "lat": "23.125712",
})


json = JsonUtil.toJson(params)
# print(UrlUtil.quote(json))
print("{\"action\":\"ipv\",\"countryCode\":\"CN\",\"cpuCore\":\"4\",\"cpuMaxHz\":\"2265600\",\"from\":\"search\",\"id\":\"570083263564\",\"item_id\":\"570083263564\",\"latitude\":\"23.125712\",\"list_type\":\"search\",\"longitude\":\"113.334662\",\"osVersion\":\"23\",\"phoneType\":\"Nexus 5\",\"search_action\":\"initiative\",\"soVersion\":\"2.0\",\"utdid\":\"XW/eOqol6igDAO6KQj0b4Q3e\"}")

# print(JsonUtil.toJson({"abc":None}))