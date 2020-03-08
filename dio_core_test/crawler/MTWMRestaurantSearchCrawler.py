# 餐厅跑数脚本

import time

from dio_core.network.downloader import Setting, Downloader


kwargs = [{"keyword": "干捞螺蛳粉", "lat": "23125756", "lng": "113264385"}]


for kwarg in kwargs:
    setting = Setting()
    setting.headers["Host"] = "i.waimai.meituan.com"
    setting.headers["Accept"] = "application/json"
    setting.headers[
        "Referer"] = "https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType=11002&entranceId=0&keyword=%E5%B9%B2%E6%8D%9E%E8%9E%BA%E8%9B%B3%E7%B2%89&qwTypeId=11002&mode=1"
    setting.headers["Origin"] = "https://h5.waimai.meituan.com"
    setting.headers[
        "User-Agent"] = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36"
    setting.headers["Content-Type"] = "application/x-www-form-urlencoded"
    setting.headers[
        "Cookie"] = "uuid=86f1d5d1-b229-4c12-a7bd-10dc5ef16e45; terminal=i; utm_source=; au_trace_key_net=default; wm_order_channel=default; _lx_utm=utm_source%3D60066; w_token=Qy1uY6h0RnVOU73sk3xFEAYn9EsAAAAA5wgAAOe8BzkBC_CqjTAFX4W2RnmK7ZF9TKNcPV8HuP7MoY8V0BrOiUilE8Gmjv_IzPBsyA; w_utmz=\"utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)\"; w_actual_lat=23125756; w_actual_lng=113334698; openh5_uuid=16d14d36a98c8-0e53a36f17ba0e-1a201708-1fa400-16d14d36a98c8; w_latlng=23129112,113264385; cssVersion=4c2d803d; w_visitid=49523e1f-aa20-46a9-b219-4907cd3201be"
    setting.headers["Accept-Encoding"] = "gzip, deflate"
    setting.headers["Connection"] = "keep-alive"
    downloader = Downloader(setting=setting)
    post_data = {}
    post_data["geoType"] = "2"
    post_data["cityId"] = "1"
    post_data["secondCategoryId"] = ""
    post_data["start"] = "0"
    post_data["queryType"] = "11002"
    post_data["keyword"] = kwarg["keyword"]
    post_data["categoryType"] = ""
    post_data["entranceId"] = "0"
    post_data["uuid"] = "16d14d36a98c8-0e53a36f17ba0e-1a201708-1fa400-16d14d36a98c8"
    post_data["platform"] = "3"
    post_data["partner"] = "4"
    post_data[
        "originUrl"] = "https://h5.waimai.meituan.com/waimai/mindex/searchresults?queryType=11002&entranceId=0&keyword=%E5%B9%B2%E6%8D%9E%E8%9E%BA%E8%9B%B3%E7%B2%89&qwTypeId=11002&mode=1"
    post_data["riskLevel"] = "71"
    post_data["optimusCode"] = "10"
    post_data["wm_latitude"] = "0"
    post_data["wm_longitude"] = "0"
    post_data["wm_actual_latitude"] = kwarg["lat"]
    post_data["wm_actual_longitude"] = kwarg["lng"]
    post_data["openh5_uuid"] = "16d14d36a98c8-0e53a36f17ba0e-1a201708-1fa400-16d14d36a98c8"
    post_data[
        "_token"] = "eJxNUGmvokAQ/C8kvC8aYRCHweRlI5fiE08OdbMfkFtBrsEBN/vfF/e9zW7S6aqurlQ6/ZOqdJ+aAhYILBhSj6CiphQYsSNIDSlc95sJRCxAggjFCTekvP80xLKQF4fUpbIVavp9AvmhIMAfL2Hfz/+Ef4zj+3o59N5AxRgX9ZRh4smIuEnmJqMsSHDj3kdenjGfEpMldz9omTpwKy+ugrpJcf2tbIKqM7sieAeAZbm34I4r9+4Fuv/Ovt2CjuSV/06rE1oSaYmjVUgjhRZVWkWvLs3+EImWxrQqvAxIfCvJK68P+EzMcr8P759A9edmZn9uj7cvdL8Q/52N/mu9t06ie8+CZZdaFt6Q58x6zJrDw8LXlrkl+1NirZbSiVR51zm4Wl80s4ULVpYJP7P1rWWfyQIqC6Kmq72fdXVIkIC4y/yM7LEhGTA84iZXLQ191BVqrFMhzT2QzVa7JIj2RaR0YvSwP6CpMAEumG0mjrMwDLtBZYukzKXNDmXHQ1h7Wnx4cLvYHOiJH0XqdbUmh3ItmLUcj2WD1StNKURyb5W0wNf9HGisYCfOLZ3LaWs99Q3gUo/buCJuwQRpeWsd160bzU9m3ux5pxyHnOkQfCbl9jLDoXZUtxfbdUVncSaG6hW6D4t6j4SPmbhLS8XYjTOdTxprIifbwXMjLGT+3MXXj1zgY/MhdSDcAmPHGaI7c9aAXGSzAp69bg3gQDO+DxrArfy7qihATlXPwppaOjwyFo4iePMbTpoQXnhYBshYzS2Wq7VlY2pB1MLI3sMtM0+XT7yz8vNpDE+BAuBC1hTfIclZRLxfXRvq129XkPn8"
    print(downloader.post("http://i.waimai.meituan.com/openh5/search/poi", data=post_data).text)
    time.sleep(3)