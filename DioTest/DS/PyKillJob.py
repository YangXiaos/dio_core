from DioCore.Network.Downloader import Downloader
from DioCore.Utils import FileUtil, TimeUtil

rows = FileUtil.readRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/kill_job_urls.txt")
for row in rows:
    url = "http://api.rhino.datatub.com/common/job/kill?job_id={}&token=5fa92f2a597cc60201780504be1028a7".format(row)
    res = Downloader.get(url)
    print(row, res.text, url)
    TimeUtil.sleep(3)