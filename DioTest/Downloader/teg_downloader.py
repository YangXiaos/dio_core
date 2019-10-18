# @Time         : 18-2-13 下午8:46
# @Author       : DioMryang
# @File         : test_downloader.py
from unittest import TestCase


# @Description  :
from DioCore.Network.Downloader import Downloader
from DioCore.Network.Downloader.Downloader import Setting


page = 0
while True:
    url = ("https://www.google.com/search?q=经贸磋商&tbs=cdr:1,cd_min:1/21/2019,cd_max:1/" +
           "28/2019&tbm=nws&start={}")
    setting = Setting()
    setting.setProxies("116.31.102.3", "57003")

    soup = Downloader.getWithBs4(url.format(page), setting=setting).soup

    result = soup.select(".l.lLrAF")
    if not result:
        break
    for aTag in soup.select(".l.lLrAF"):
        print(aTag["href"])
    page += 10
    print()
