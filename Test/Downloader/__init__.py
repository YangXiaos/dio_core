# @Time         : 18-2-13 下午8:51
# @Author       : DioMryang
# @File         : Const.py.py
# @Description  :
import re
from queue import Queue

from DioCore.Network.Downloader.Downloader import Downloader, Setting

from DioCore.Utils import ThreadUtil, TextUtil

mapping = {}
q = Queue()

# 多线程 ts downloader

class TsDownloader(object):

    def __init__(self, m3u8: str=None):
        self.m3u8 = m3u8 if m3u8 is not None else ""

    def getM3u8(self) -> str:
        """"""
        return ""

    def getTsList(self):
        """获取ts列表"""

def init(url):
    soup = Downloader.getWithBs4(url).soup
    m3u8_url = soup.select_one(".yunbofang video").attrs["src"]

    s = Setting()
    s.returnFailReq = True
    text = Downloader.get(m3u8_url, setting=s).text
    result = TextUtil.getAllMatch("index\d+.ts", text)
    ts = result[-1]

    d = TextUtil.getFirstMatch(ts, "(\d+)")

    url_front = m3u8_url.split("index")[0]
    for i in range(int(d) + 1):
        q.put({
            "url": url_front + "index" + str(i) + ".ts",
            "ind": i
        })


def download(thread):
    while True:
        if q.empty():
            break
        msg = q.get()
        print("{} 跑数 {}".format(thread, msg["ind"]))
        res = Downloader.get(msg["url"])
        mapping[msg["ind"]] = res.content


init("http://sgzxt.com/play/4024-1-1.html")
ThreadUtil.multiThreadRun(download, 7)

content = bytes()
for key in sorted(mapping.keys()):
    content = content + mapping[key]

file = open("miao.3.ts", "wb")
file.write(content)
file.close()