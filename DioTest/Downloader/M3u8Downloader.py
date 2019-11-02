from queue import Queue

from DioCore.Network.Downloader import Downloader
from DioCore.Utils import TextUtil, ThreadUtil


class M3u8Downloader(object):


    def __init__(self, m3u8):
        self.m3u8 = m3u8
        self.tsUrls = self.getTsUrls()
        self.queue = Queue()
        self.data = {}

        for tsInd, ts in self.tsUrls:
            if tsInd == 15:
                break
            self.queue.put({"tsInd": tsInd, "url": self.m3u8.replace("index.m3u8", ts)})

        self.max = tsInd
        ThreadUtil.multiThreadRun(self.downloadTs, 5)

        file = open("dio.ts", "wb")
        for ind in range(tsInd):
            if ind in self.data:
                file.write(self.data[ind])
            else:
                print("异常索引", ind)
        file.close()

    def downloadTs(self, threadNum):
        while not self.queue.empty():
            ts = self.queue.get()
            try:
                print(threadNum, "下载ts", ts)
                ind = ts["tsInd"]
                res = Downloader.get(ts["url"])
                self.data[ind] = res.content
            except Exception as e:
                print("下载异常", e, ts)

    def getTsUrls(self):

        res = Downloader.get(self.m3u8)
        result = TextUtil.getAllMatch("#EXTINF:.*,\n(.*)", res.text)
        return zip(range(len(result)), result)


if __name__ == '__main__':
    m3u8 = M3u8Downloader("http://bobo.kkpp.space/20170704/4vG3oTcJ/hls/index.m3u8")

