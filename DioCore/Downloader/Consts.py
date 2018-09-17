# @Time         : 18-5-15 下午10:40
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
