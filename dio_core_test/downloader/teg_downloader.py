# @Time         : 18-2-13 下午8:46
# @Author       : DioMryang
# @File         : test_downloader.py
from unittest import TestCase


# @Description  :
from dio_core.network.downloader import Downloader
from dio_core.network.downloader.downloader import Setting


page = 0
while True:
    url = ("https://www.google.com/search?q=经贸磋商&tbs=cdr:1,cd_min:1/21/2019,cd_max:1/" +
           "28/2019&tbm=nws&start={}")
    setting = Setting()
    setting.set_proxies("116.31.102.3", "57003")

    soup = Downloader.get_with_bs4(url.format(page), setting=setting).soup

    result = soup.select(".l.lLrAF")
    if not result:
        break
    for aTag in soup.select(".l.lLrAF"):
        print(aTag["href"])
    page += 10
    print()
