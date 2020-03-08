import ftplib
import json

from dio_core.utils import md5_util

config = {
    "hostName": "120.31.140.156",
    "port": "21",
    "user": "datastory",
    "pwd": "datastoryFtp@2016",
    "ftpDirPath": "/pic_result"
}

rows = json.load(open("/home/changshuai/Back/PythonProject/PyWork/data/ftp_seeds.json"))[:10000]

f = ftplib.FTP(config["hostName"])
f.login(config["user"], config["pwd"])
f.cwd("/pic_result/")
mapping = {}
for dir_ in f.nlst():
    if len(dir_) < 30:
        f.cwd("/pic_result/" + dir_)
        mapping[dir_] = f.nlst()

f.close()
success = 0

for row in rows:
    if md5_util.md5("{}_datatub_{}".format(row["item_id"], row["url"])) in mapping[row["nextDirName"]]:
        success += 1

print(success)
