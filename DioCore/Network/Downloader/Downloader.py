# @Time         : 18-1-20 下午1:56
# @Author       : DioMryang
# @File         : Downloader.py
# @Description  :
import logging
import traceback
from typing import Union

import chardet
import requests
from bs4 import BeautifulSoup
from requests import Response

from DioCore import Const
from DioCore.Network.Downloader.Error import StateCodeException


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
    def resetSession(self):
        """重设 session"""
        self.session = requests.Session()

    def __init__(self,
                 request: str="GET",
                 timeout: int=Const.DEFAULT_PARAM_TIMEOUT,
                 headers: dict=Const.DEFAULT_HEADERS,
                 returnFailResponse: bool=Const.DEFAULT_PARAM_RETURN_FAIL_RESPONSE,
                 repeat: int=Const.DEFAULT_REPEAT,
                 ua: str=Const.DEFAULT_HEADER_USER_AGENT,
                 htmlParse=False,
                 proxies=None):

        self.request = request
        self.ua = ua
        self.headers = headers
        self.repeat = repeat
        self.timeout = timeout
        self.returnFailReq = returnFailResponse
        self.htmlParse = htmlParse

        self.session = requests.Session()
        self.headers.update({Const.PARAM_USER_AGENT: self.ua})
        self.proxies = proxies

    def setParams(self, **kwargs):
        """设置请求参数"""
        if Const.PARAM_TIMEOUT in kwargs:
            self.timeout = kwargs.get(Const.PARAM_TIMEOUT)
        if Const.PARAM_HEADERS in kwargs:
            self.headers = kwargs.get(Const.PARAM_HEADERS)
        if Const.PARAM_USER_AGENT in kwargs:
            self.ua = kwargs.get(Const.PARAM_USER_AGENT)
            self.headers.update({Const.PARAM_USER_AGENT: self.ua})
        if Const.PARAM_REPEAT in kwargs:
            self.repeat = kwargs.get(Const.PARAM_REPEAT)
        if Const.DEFAULT_PARAM_RETURN_FAIL_RESPONSE in kwargs:
            self.returnFailReq = kwargs.get(Const.DEFAULT_PARAM_RETURN_FAIL_RESPONSE)
        if Const.PARAM_PROXIES in kwargs:
            self.proxies = kwargs.get(Const.PARAM_PROXIES)

    def setProxies(self, ip, port):
        proxyDict = {
            "http": "http://{}:{}".format(ip, port),
            "https": "https://{}:{}".format(ip, port)
        }
        self.proxies = proxyDict

    def getReqParams(self) -> dict:
        """ 返回 requests 的请求参数"""
        params = {
            Const.PARAM_HEADERS: self.headers,
            Const.PARAM_TIMEOUT: self.timeout
        }
        if self.proxies is not None:
            params[Const.PARAM_PROXIES] = self.proxies
        return params


class Downloader(object):
    PARSER = "lxml"
    logger = logging.getLogger("Downloader")

    @classmethod
    def request(cls, url: str, data: Union[str, dict]=None, setting: Setting=None) -> Response:
        if setting is None:
            setting = Setting()
        cls.logger.info("请求 {}".format(url))

        # 失败重复请求
        for i in range(setting.repeat):
            try:
                # 请求url
                res = requests.request(setting.request, url, data=data, **setting.getReqParams())

                # 请求code判定
                if setting.returnFailReq or res.status_code != 200:
                    raise StateCodeException("error code {}".format(res.status_code))

                # 解析页面
                if setting.htmlParse:
                    res.encoding = chardet.detect(res.content)["encoding"]
                    res.soup = BeautifulSoup(res.text, cls.PARSER)
                    res.setting = setting
                return res
            except Exception as ignored:
                cls.logger.error("第{}次 请求失败".format(i+1))
                traceback.print_exc()

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

        cls.logger.info("请求 {}".format(url))
        for i in range(setting.repeat):
            try:
                res = requests.get(url, **setting.getReqParams())
                if setting.returnFailReq or res.status_code != 200:
                    raise StateCodeException("error code {}".format(res.status_code))
                if setting.htmlParse:
                    res.encoding = chardet.detect(res.content)["encoding"]
                    res.soup = BeautifulSoup(res.text, cls.PARSER)
                    res.setting = setting
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

    @classmethod
    def getBs4(cls, url: str, setting: Setting=None) -> BeautifulSoup:
        if setting is None:
            setting = Setting()
            setting.htmlParse = True
        else:
            setting.htmlParse = True
        return cls.get(url, setting=setting).soup

    @classmethod
    def getJson(cls, url: str, setting: Setting=None) -> dict:
        return cls.get(url, setting=setting).json()

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
        res = Downloader.get(url, session, reqKwargs, **kwargs)
        return res, res.content, url.split("/")[-1], url.split(".")[-1]

    @classmethod
    def payload(cls, url, data: str="", setting: Setting=None) -> Response:
        """
        payload 请求
        :param url: 请求url
        :param data: 数据
        :param setting: 请求配置
        :return:
        """
        if setting is None:
            setting = Setting()
            setting.request = "POST"

        return cls.request(url, data, setting=setting)

    def __init__(self):
        self.setting = Setting()

    def resetSession(self):
        """
        重新设置 session    
        :return:
        """
        self.session = requests.Session()


class Middleware(object):
    """"""
    def before(self):
        pass

    def after(self):
        pass



if __name__ == '__main__':
    res_ = Downloader.get(url="http://pdfm2.eastmoney.com/EM_UBG_PDTI_Fast/api/js?id=0001211&TYPE=k&rtntype=5&isCR=false&authorityType=fa")

    print(res_.text)
