import traceback

import requests

from DioCore.Utils import DateTimeUtil, RandomUtil

url = "https://www.amazon.com/s"

querystring = {"k":"HUAWEI","ref":"nb_sb_noss_2"}

headers = {
    'cookie': 'session-id=134-1234567-4352220; session-id-time=2082787201l; i18n-prefs=USD; lc-main=zh_CN; sp-cdn="L5Z9:CN"; ubid-main=131-0190743-9442673; session-token=MwapxtBGwqHY2CE67riIX3ZwTiN5HkkmSHuMRzLmToNq2+tIw5+u4Qj1I8PHS6HtuAp1GAxRWpYKmd9ufAhmNyCxl5Xgc04T2/sWZC9WVrEx+Hou/tDTpUvd7Ymg3QrslJaBPztw8UGDMtRgkJespSU4feRmCOcyPCLKnRZA49EJKIX6t3wx5rNw5qJTErPU; arp_scroll_position=5052; x-amz-captcha-1=1559653816460430; x-amz-captcha-2=wge3ppz+VxIkD9HveGMBnQ==; csm-hit=tb:s-19J91GZBADJWTAASH3NY|1559646617897&t:1559646618717&adb:adblk_no; x-wl-uid=15CrSUt+leHUfZGa7xqDIaO/11njpq87Xn9dO2lmWBh6JkDH5D5PdCryYD5bBH1a1UgKxi0ZbpIg=',
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'cache-control': "max-age=0",
    'authority': "www.amazon.com",
    'referer': "https://www.amazon.com/",
    'Host': "www.amazon.com",
    'Connection': "keep-alive"
    }


session = requests.Session()


i, fail = 0, 0
print("开始时间 {}".format(DateTimeUtil.getCurrentDatetime()))
while True:
    i += 1
    print(i)
    try:
        if fail > 4:
            break
        proxies = {
            'http': 'http://60.182.176.145:56066',
            'https': 'https://60.182.176.145:56066'
        }
        kwargs = {
            "url": RandomUtil.getRandomEleFromList(),
            "proxies": proxies,
            "headers": headers,
            "params": querystring,
            "timeout": 15
        }

        response = session.get(**kwargs)
        if "we just need to make sure you're not a robo" in response.text:
            print("fail")
            fail += 1

        print(len(response.text))
        print(response.cookies)
    except Exception as e:
        traceback.print_exc()
print("时间 {}".format(DateTimeUtil.getCurrentDatetime()))
