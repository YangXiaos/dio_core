from typing import Union

import requests

from DioCore import Const


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

    GET = "GET"
    POST = "POST"

    def resetSession(self):
        """重设 session"""
        self.session = requests.Session()

    def __init__(self,
                 request: str=GET,
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

    def setParams(self, **kwargs) -> None:
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

    def setProxies(self, ip:str, port: Union[str, int]) -> None:
        """设置代理"""
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
