# @Time         : 18-1-20 下午1:56
# @Author       : DioMryang
# @File         : Downloader.py
# @Description  :
import traceback

import chardet
import requests
from bs4 import BeautifulSoup
from requests import Response

from DioCore.Downloader import Consts
from DioCore.Downloader.Error import StateCodeException


# 超时时间
TIMEOUT = 30

# 浏览器伪装头
UA = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 " +
      "Safari/537.36")

# 请求头
HEADERS = {
    "User-Agent": UA
}

# 失败重试次数
REPEAT = 3


class Setting(object):
    """
    attributes:
        ua: 浏览器头
        headers: 请求头
        timeout: 超时
        returnFailReq: 返回错误请求
        repeat: 重复次数

    GlobalAttributes:


    """

    class FIELDS_CONST(object):
        TIMEOUT = "timeout"
        HEADERS = "headers"
        UA = "ua"
        REPEAT = "repeat"
        RETURN_FAIL_REQ = "returnFailReq"

        USER_AGENT = "User-Agent"

    def __init__(self, timeout: int=TIMEOUT, headers: dict=HEADERS, returnFailReq: bool=False, repeat: int=REPEAT,
                 ua: str=UA, htmlParse=False):
        self.ua = ua
        self.headers = headers
        self.repeat = repeat
        self.timeout = timeout
        self.returnFailReq = returnFailReq
        self.htmlParse = htmlParse

        self.session = requests.Session()
        self.headers.update({self.FIELDS_CONST.USER_AGENT: self.ua})

    def resetSession(self):
        """重设 session"""
        self.session = requests.Session()

    def setParams(self, **kwargs):
        """设置请求参数"""
        if self.FIELDS_CONST.TIMEOUT in kwargs:
            self.timeout = kwargs.get(self.FIELDS_CONST.TIMEOUT)

        if self.FIELDS_CONST.HEADERS in kwargs:
            self.headers = kwargs.get(self.FIELDS_CONST.HEADERS)
        if self.FIELDS_CONST.UA in kwargs:
            self.ua = kwargs.get(self.FIELDS_CONST.UA)
            self.headers.update({self.FIELDS_CONST.USER_AGENT: self.ua})
        if self.FIELDS_CONST.REPEAT in kwargs:
            self.repeat = kwargs.get(self.FIELDS_CONST.REPEAT)
        if self.FIELDS_CONST.RETURN_FAIL_REQ in kwargs:
            self.returnFailReq = kwargs.get(self.FIELDS_CONST.RETURN_FAIL_REQ)

    def getReqParams(self) -> dict:
        """ 返回 requests 的请求参数"""
        return {
            self.FIELDS_CONST.HEADERS: self.headers,
            self.FIELDS_CONST.TIMEOUT: self.timeout
        }


class Downloader(object):
    PARSER = "lxml"

    @classmethod
    def get(cls, url: str, setting: Setting=None) -> Response:
        """
        通过会话请求链接, 返回响应结果
        :param setting:
        :param url: 请求 url
        :return: 响应结果
        """
        if setting is None:
            setting = Setting()

        for i in range(setting.repeat):
            try:
                res = requests.get(url, **setting.getReqParams())
                if setting.returnFailReq or res.status_code != 200:
                    raise StateCodeException("error code {}".format(res.status_code))
                if setting.htmlParse:
                    res.encoding = chardet.detect(res.content)["encoding"]
                    res.soup = BeautifulSoup(res.text, cls.PARSER)
                return res
            except Exception as ignored:
                print("第{}次 请求失败".format(i+1))
                traceback.print_exc()

    @classmethod
    def getWithBs4(cls, url: str, setting: Setting=None) -> Response:
        if setting is None:
            setting = Setting()
            setting.htmlParse = True
        else:
            setting.htmlParse = True
        return cls.get(url, setting=setting)

    @staticmethod
    def getFile(url, session=None, reqKwargs=None, **kwargs):
        """
        请求 获取文件
        :param url:
        :param session:
        :param reqKwargs:
        :param kwargs:
        :return:
        """
        res = Downloader.getRes(url, session, reqKwargs, **kwargs)
        return res, res.content, url.split("/")[-1], url.split(".")[-1]

    def __init__(self):
        self.setting = Setting()

    def resetSession(self):
        """
        重新设置 session
        :return:
        """
        self.session = requests.Session()


if __name__ == '__main__':
    res_ = Downloader.get("http://blog.csdn.net/u014756517/article/details/51953420")
    print(res_.text)
