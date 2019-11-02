from DioCore.Network.Downloader import Setting, Downloader

setting = Setting()
setting.headers["Host"] = "i.waimai.meituan.com"
setting.headers["Connection"] = "close"
setting.headers["Content-Length"] = "1712"
setting.headers["Accept"] = "application/json"
setting.headers["Origin"] = "https://h5.waimai.meituan.com"
setting.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
setting.headers["Content-Type"] = "application/x-www-form-urlencoded"
setting.headers["Referer"] = "https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId=880752952881352&utm_source=&source=shoplist&initialLat=&initialLng=&actualLat=23.125764&actualLng=113.334692"
setting.headers["Accept-Encoding"] = "gzip, deflate"
setting.headers["Accept-Language"] = "zh-CN,zh;q=0.9"
setting.headers["Cookie"] = ("_lxsdk_cuid=16c7503f4cfc8-02f35835186a28-1a201708-1fa400-16c7503f4cfc8; _ga=GA1.3.123527420.1565331289; terminal=i; w_utmz=\"utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)\"; w_uuid=fDIP39SlRhmsUxl1ufq_HGxtvITS6s7lqU2tnWCZzZR2Kw0OkQiE0exCXh7wAV4O; utm_source=0; wx_channel_id=0; webp=1; utm_source=; OUTFOX_SEARCH_USER_ID_NCOO=319032372.8529649; __mta=213671211.1565331291465.1565683151305.1565770974086.4; iuuid=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340; mt_c_token=Qy1uY6h0RnVOU73sk3xFEAYn9EsAAAAA5wgAAOe8BzkBC_CqjTAFX4W2RnmK7ZF9TKNcPV8HuP7MoY8V0BrOiUilE8Gmjv_IzPBsyA; oops=Qy1uY6h0RnVOU73sk3xFEAYn9EsAAAAA5wgAAOe8BzkBC_CqjTAFX4W2RnmK7ZF9TKNcPV8HuP7MoY8V0BrOiUilE8Gmjv_IzPBsyA; userId=125898618; _lxsdk=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340; w_token=Qy1uY6h0RnVOU73sk3xFEAYn9EsAAAAA5wgAAOe8BzkBC_CqjTAFX4W2RnmK7ZF9TKNcPV8HuP7MoY8V0BrOiUilE8Gmjv_IzPBsyA; openh5_uuid=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340; uuid=b87e7a35e6cc43c0ace7.1565953580.1.0.0; au_trace_key_net=default; openh5_uuid=2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340; __mta=213671211.1565331291465.1565953569081.1567846775487.5; wm_order_channel=default; _gid=GA1.3.2120311235.1568012430; mtsi-cur-time=\"2019-09-09 15:00:42\"; w_visitid=068b9f56-7e64-4295-a950-59b0fea4a38d; cssVersion=2ef84fdd; _lx_utm=utm_source%3D; _lxsdk_s=16d15722ecd-786-3f5-dd2%7C125898618%7C5; w_latlng=24777226,113678685; w_actual_lat=0; w_actual_lng=0")


downloader = Downloader(setting=setting)
postData = {}
postData["lng"] = ""
postData["lat"] = ""
postData["gpsLng"] = "113.334692"
postData["gpsLat"] = "23.125764"
postData["shopId"] = "0"
postData["mtWmPoiId"] = "880752952881352"
postData["startIndex"] = "0"
postData["labelId"] = "0"
postData["scoreType"] = "0"
postData["uuid"] = "2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340"
postData["platform"] = "3"
postData["partner"] = "4"
postData["originUrl"] = "https://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId=880752952881352&utm_source=&source=shoplist&initialLat=&initialLng=&actualLat=23.125764&actualLng=113.334692"
postData["riskLevel"] = "71"
postData["optimusCode"] = "10"
postData["wm_latitude"] = "24777226"
postData["wm_longitude"] = "113678685"
postData["wm_actual_latitude"] = "0"
postData["wm_actual_longitude"] = "0"
postData["openh5_uuid"] = "2E42332BF3FA3E12F5CFCFA99E799888E8883DB85EF252B10CB184761FFDB340"
postData["_token"] = ("eJxV0mmPqjoYAOD/wge/SKQtlGUSc6MCKo4LIOp4MrlhlUWWkYqjJ+e/n6ojuTch6cO7UQq/mdM0YN4ggBKALNOEJ+aNgT3Q"
                      "ExmWITXNYFEGiMcSAAIt8P8Xw7KksIx32qjM2y8sK6yC4Oc9YNH7X1BBgIVABp/syzz+ZJFAr3vVlBYxMSFV/cZxMe5d3CR3"
                      "k14eJuTsFj2/zLlniMuTIgi/uTwszv8ElR2X1TTod3LyI1kGEkYKRrIMeYw6Z5L/W5fnkx/2Oz9rTSuPSU06SZGQxD2+u6Tf"
                      "ujj0O65PH/oII74HEZZE4RWjaQj5Hs8LooLosTB08/n6vnkeCCzEAo3xgG+FWsFW9OUxpkKKQiU+hKnkh2iHCO+SZSrhoXtM"
                      "ukuidRJ6iE6RHr2iyEIZPESfK/OtpJcU2Aq3emURAK1QK6GV2Ep+CbYd8DmZfkX47MVUzx1IVM8pCtVjigSp5PuRZfcjo6v7"
                      "36Nj1enmniSv5Jz+f7SvTg4FVWhcSabrzeE6cOJIeZ/wsTOwdN+s9l+LbWHH151X19F4tplfB/ZS8BqlC6VNdU755rBTz4I/"
                      "VSKDdOXSz21tmq6H6co5mS6p/A8gpPZiXhvjiuwWoSDlH4OZVsJLkn0Lc1NZHq5Eu8SFMba0kQNcM8dmgCb6PhgFxtEyZvZm"
                      "sg6z+rQeV1uYb5VbtJxhKTPL0tADYXPYOOBjthva+jHJVvMFbGxS5vUwNfeNfhTxWsvmWISSh/ncMS/JuhGa9OBsC6siYwt4"
                      "Va2ayK2QcYP7mix5Z4+uzi4UJXGnX7SurYvDCC64zL4txtJ+K24sIwrMblhGjuqKXyPPdzYQ2udJVW5jAXVHelfmv2f5/gC3"
                      "t/VC0/QF53sjS685rxly29iqs2/5C3kwWO2qwQisrr6mhWoYNWCsrzhVGdtLLFiT0eB9fi52hzQ81lF3EYYgnS1tP+vexs0q"
                      "UtV0Sub1HPCG6SJu0O8zf/4COoo2Jw==")

print(downloader.post("http://i.waimai.meituan.com/openh5/poi/comments", data=postData).text)
