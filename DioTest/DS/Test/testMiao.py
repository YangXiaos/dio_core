import time

import requests

from DioCore.Utils import LoggerUtil

url = "https://search.jd.com/Search"

querystring = {"keyword":"儿童奶酪 Anna","enc":"utf-8","psort":"","qrst":"1","page":"1","s":"1"}

headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    # 'Host': "search.jd.com",
    # 'Connection': "keep-alive"
    }


i = 0
while True:
    i += 1
    time.sleep(1)
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.encoding = "utf-8"
    logger = LoggerUtil.getLogger(__file__)
    if len(response.text) < 200000:
        logger.info(response.text)

    logger.info("第{}次请求，页面长度{}, YN {}".format(i, len(response.text), "棒500g原味" in response.text))
