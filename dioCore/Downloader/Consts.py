# @Time         : 18-1-25 下午10:55
# @Author       : DioMryang
# @File         : Consts.py
# @Description  :

from enum import Enum, unique


@unique
class DownloaderType(Enum):
    Res = "getRes"
    Soup = "getSoup"
    Json = "getJson"
    File = "getFile"
    Post = "post"
    Driver = "getDriver"


# 超时时间
TIMEOUT = 30

# 浏览器伪装头
UA = "Mozilla/5.0"

# 请求头
HEADERS = {
    "User-Agent": UA
}

# 重试次数
REPTY_TIME = 3

# 请求成功码
SUCCESS_STATE_CODE = 200

PARSER = "lxml"

