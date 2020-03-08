import time

from dio_core.network.downloader.downloader import Downloader
from dio_core.utils import file_util

rows = list(file_util.readRows("/home/changshuai/PycharmProjects/dio_core/dio_core_test/Data/cli_kill_job_list.txt"))
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
