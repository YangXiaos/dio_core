from queue import Queue

from dio_core.network.downloader import Downloader
from dio_core.utils import thread_util
from dio_core_test.utils import text_util


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
        thread_util.multi_thread_run(self.downloadTs, 5)

        file = open("dio.ts", "wb")
        for ind in range(tsInd):
            if ind in self.data:
                file.write(self.data[ind])
            else:
                print("异常索引", ind)
        file.close()

    def downloadTs(self, thread_num):
        while not self.queue.empty():
            ts = self.queue.get()
            try:
                print(thread_num, "下载ts", ts)
                ind = ts["tsInd"]
                res = Downloader.get(ts["url"])
                self.data[ind] = res.content
            except Exception as e:
                print("下载异常", e, ts)

    def getTsUrls(self):

        res = Downloader.get(self.m3u8)
        result = text_util.get_all_match("#EXTINF:.*,\n(.*)", res.text)
        return zip(range(len(result)), result)


if __name__ == '__main__':
    m3u8 = M3u8Downloader("http://bobo.kkpp.space/20170704/4vG3oTcJ/hls/index.m3u8")

