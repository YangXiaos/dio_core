from dio_core.network.downloader import Downloader
from dio_core.utils import file_util, time_util

rows = file_util.readRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/kill_job_urls.txt")
for row in rows:
    url = "http://api.rhino.datatub.com/common/job/kill?job_id={}&token=5fa92f2a597cc60201780504be1028a7".format(row)
    res = Downloader.get(url)
    print(row, res.text, url)
    time_util.sleep(3)