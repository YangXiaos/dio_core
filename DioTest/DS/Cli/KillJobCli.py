import time

from DioCore.Network.Downloader.Downloader import Downloader
from DioCore.Utils import FileUtil

rows = list(FileUtil.readRows("/home/changshuai/PycharmProjects/dio_core/DioTest/Data/cli_kill_job_list.txt"))
# rows = ["app_ecomm_all_20190802141514_042_83", "app_ecomm_all_20190802141516_952_91"]
host = "datatub5:20425"
# host = "api.rhino.datatub.com"
for row in rows:
    try:
        res = Downloader.get("http://{}/common/job/kill?job_id={}&token=5fa92f2a597cc60201780504be1028a7"
                             .format(host,row))
        print(res.json())

    except Exception as e:
        print(e)

    time.sleep(1)
