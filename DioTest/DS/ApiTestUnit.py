import logging
import traceback

import requests

from DioCore.Utils import RandomUtil
from DioCore.Utils.LoggerUtil import getLogger


class SingleThreadApiTestUnit(object):

    def __init__(self, urls, headers, proxies, timeout=8, logFilePath=""):
        self.urls = urls
        self.headers = headers
        self.proxies = proxies
        self.timeout = timeout
        self.logger = getLogger(SingleThreadApiTestUnit)

        handlerFormat = logging.Formatter("[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s")
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(handlerFormat)

        fileHandler = logging.FileHandler(logFilePath, "a")
        fileHandler.setFormatter(handlerFormat)
        self.logger.addHandler(streamHandler)
        self.logger.addHandler(fileHandler)

    def start(self):
        session = requests.session()
        i, fail = 0, 0
        self.logger.info("开始跑数")

        while True:
            i += 1
            self.logger.info("第{}次跑数".format(i))

            try:
                if fail > 4:
                    break

                kwargs = {
                    "headers": self.headers,
                    "timeout": 15,
                    "verify" : False
                }
                url = RandomUtil.getRandomEleFromList(self.urls)
                if isinstance(url, str):
                    response = requests.get(url, headers=self.headers, proxies=self.proxies, timeout=self.timeout)
                else:
                    response = requests.post(url["url"], data=url["data"], headers=self.headers, proxies=self.proxies, timeout=self.timeout)

                if "we just need to make sure you're not a robo" in response.text:
                    self.logger.error("请求fail")
                    fail += 1
                else:
                    fail = 0

                self.logger.info("文本长度 {}".format(len(response.text)))
                self.logger.info("cookies {}".format((response.cookies)))

            except Exception as e:
                fail += 1
                traceback.print_exc()

            self.logger.info("跑数over")


headers_A = {
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'cache-control': "max-age=0",
    'authority': "www.amazon.ae",
    'Host': "www.amazon.ae",
    'Connection': "keep-alive",
    'cookie': 'session-id=262-1303045-4193915; i18n-prefs=AED; ubid-acbae=262-6047108-5915305; session-token=n6zGAJb1MUNhUE8iDgWj4hRIqdEyJwRJXYaZtRVGouLTQFcTgeg7O1DaybIgg3sUZuO0LabaJ9tZMnYMaeELRhECpSsBZPrUd6UFtLRtxDV65SIzemOhQ8kknAzLPy4rXggKs3u57801WzsQmht56PFw2l0pCX4bZkoDzBrLNl/rkOhk/6e++ng4SxeiBef4; x-wl-uid=1kflW/tx8LCgGJ7OPN+8vxeMMzcCFB++nMJgilqDejVNdJnIqrQ2JP7+IDSBtdgV1f/6AB9YRdWg=; arp_scroll_position=3968; csm-hit=tb:s-G656BQDE2CQ68X1YFT8S|1559650581877&t:1559650582222&adb:adblk_no; session-id-time=2082758401l',
    'referer': "https://www.amazon.ae/s?k=HUAWEI&page=2&qid=1559649242&ref=sr_pg_2",
}
headers_B = {
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'cache-control': "max-age=0",
    'authority': "www.amazon.ae",
    'Host': "www.amazon.ae",
    'Connection': "keep-alive",
}
headers_D = {
    'origin': "https://www.amazon.ae",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded;charset=UTF-8",
    'accept': "text/html,*/*",
    'authority': "www.amazon.ae",
    'x-requested-with': "XMLHttpRequest"
}


proxies_A = {
    'http': 'http://113.121.164.142:56038',
    'https': 'https://113.121.164.142:56038'
}
proxies_B = {
    'http': 'http://114.239.0.217:56033',
    'https': 'https://114.239.0.217:56033'
}
proxies_C = {
    'http': 'http://60.182.176.145:556066',
    'https': 'https://60.182.176.145:56066'
}

urls_A = [
    "https://www.amazon.ae/s?k=HUAWEI&ref=nb_sb_noss",
    "https://www.amazon.ae/s?k=HUAWEI&page=2&ref=sr_pg_2",
    "https://www.amazon.ae/s?k=HUAWEI&page=3&ref=sr_pg_3",
    "https://www.amazon.ae/s?k=HUAWEI&page=4&ref=sr_pg_4",
    "https://www.amazon.ae/s?k=HUAWEI&page=5&ref=sr_pg_5",
    "https://www.amazon.ae/s?k=HUAWEI&page=6&ref=sr_pg_6",
]
urls_B = [
    "https://www.amazon.ae/Huawei-Y9-2019-Dual-SIM/dp/B07MTRH1WB/ref=sr_1_1?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-1",
    "https://www.amazon.ae/Huawei-Y5-Prime-2018-Dual-SIM/dp/B07MK4PJZ4/ref=sr_1_2?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-2",
    "https://www.amazon.ae/Huawei-Y9-2019-Dual-SIM/dp/B07MJZHXHK/ref=sr_1_3?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-3",
    "https://www.amazon.ae/Huawei-Nova-3i-Dual-SIM/dp/B07L9ZM5VD/ref=sr_1_4?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-4",
    "https://www.amazon.ae/Huawei-Nova-3i-Dual-SIM/dp/B07L9Z32Y8/ref=sr_1_5?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-5",
    "https://www.amazon.ae/Huawei-Mate-20-Dual-Sim/dp/B07MTQP71D/ref=sr_1_6?keywords=HUAWEI&qid=1559715452&s=gateway&smid=A2KKU8J8O8784X&sr=8-6",
    "https://www.amazon.ae/Huawei-MATE-PRO-Dual-Sim/dp/B07MTR62G3/ref=sr_1_7?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-7",
    "https://www.amazon.ae/Huawei-Mate-Pro-Dual-Sim/dp/B07MK4K9CR/ref=sr_1_8?keywords=HUAWEI&qid=1559715452&s=gateway&smid=A2KKU8J8O8784X&sr=8-8",
    "https://www.amazon.ae/Huawei-Mate-Lite-Dual-SIM/dp/B078MRW4Q6/ref=sr_1_9?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-9",
    "https://www.amazon.ae/Huawei-Prime-2018-Dual-SIM/dp/B07L9Z8KHH/ref=sr_1_10?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-10",
    "https://www.amazon.ae/Huawei-Y9-2019-Dual-SIM/dp/B07MTRSNRM/ref=sr_1_11?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-11",
    "https://www.amazon.ae/Huawei-Mate-Pro-Dual-Sim/dp/B07MTRT5K1/ref=sr_1_12?keywords=HUAWEI&qid=1559715452&s=gateway&sr=8-12",
    "https://www.amazon.ae/Huawei-MATE-20-Dual-Sim/dp/B07MTSDSP3/ref=sr_1_13?keywords=HUAWEI&qid=1559715452&s=gateway&smid=A2KKU8J8O8784X&sr=8-13",
    "https://www.amazon.ae/Huawei-Mate-20-Dual-Sim/dp/B07MTRM2J2/ref=sr_1_14?keywords=HUAWEI&qid=1559715452&s=gateway&smid=A2KKU8J8O8784X&sr=8-14",
]
urls_C = [
    {
        "data": "sortBy=&reviewerType=all_reviews&formatType=&mediaType=&filterByStar=&pageNumber=1&filterByLanguage=&filterByKeyword=&shouldAppend=undefined&deviceType=desktop&reftag=cm_cr_getr_d_paging_btm_prev_1&pageSize=10&asin=B01N2VMGT6&scope=reviewsAjax1",
        "url": "https://www.amazon.ae/hz/reviews-render/ajax/reviews/get/ref=cm_cr_getr_d_paging_btm_prev_1",
        "method": "POST",
    },
    {
        "data": "sortBy=&reviewerType=all_reviews&formatType=&mediaType=&filterByStar=&pageNumber=2&filterByLanguage=&filterByKeyword=&shouldAppend=undefined&deviceType=desktop&reftag=cm_cr_getr_d_paging_btm_next_2&pageSize=10&asin=B01N2VMGT6&scope=reviewsAjax4",
        "url": "https://www.amazon.ae/hz/reviews-render/ajax/reviews/get/ref=cm_cr_getr_d_paging_btm_next_2",
        "method": "POST",
    },
    {
        "data": "sortBy=recent&reviewerType=all_reviews&formatType=&mediaType=&filterByStar=&pageNumber=1&filterByLanguage=&filterByKeyword=&shouldAppend=undefined&deviceType=desktop&reftag=cm_cr_arp_d_viewopt_srt&pageSize=10&asin=B07NWBVQWK&scope=reviewsAjax0",
        "url": "https://www.amazon.ae/hz/reviews-render/ajax/reviews/get/ref=cm_cr_arp_d_viewopt_srt",
        "method": "POST",
    },
    {
        "data": "sortBy=recent&reviewerType=&formatType=&mediaType=&filterByStar=&pageNumber=1&filterByLanguage=&filterByKeyword=&shouldAppend=undefined&deviceType=desktop&reftag=cm_cr_arp_d_viewopt_srt&pageSize=10&asin=B07MTRSNRM&scope=reviewsAjax0",
        "url": "https://www.amazon.ae/hz/reviews-render/ajax/reviews/get/ref=cm_cr_arp_d_viewopt_srt",
        "method": "POST",
    },
]


# 搜索接口
kwargs_A = {
    "headers": headers_A,
    "proxies": proxies_A,
    "urls": urls_A
}
# 商品接口
kwargs_B = {
    "headers": headers_B,
    "proxies": proxies_B,
    "urls": urls_B,
    "logFilePath": "amazon.ae_B.log"
}
# 评论接口
kwargs_C = {
    "headers": headers_D,
    "proxies": proxies_C,
    "urls": urls_C,
    "logFilePath": "amazon.ae_C.log"
}


# testunit = SingleThreadApiTestUnit(**kwargs_A)
# testunit = SingleThreadApiTestUnit(**kwargs_B)
testunit = SingleThreadApiTestUnit(**kwargs_C)
testunit.start()
