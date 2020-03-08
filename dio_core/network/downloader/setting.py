from typing import Union

import requests

from dio_core import const


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

    def reset_session(self):
        """重设 session"""
        self.session = requests.Session()

    def __init__(self,
                 request: str = GET,
                 timeout: int = const.DEFAULT_PARAM_TIMEOUT,
                 headers: dict = const.DEFAULT_HEADERS,
                 return_fail_response: bool = const.DEFAULT_PARAM_RETURN_FAIL_RESPONSE,
                 repeat: int = const.DEFAULT_REPEAT,
                 ua: str = const.DEFAULT_HEADER_USER_AGENT,
                 html_parse=False,
                 proxies=None):

        self.request = request
        self.ua = ua
        self.headers = headers
        self.repeat = repeat
        self.timeout = timeout
        self.returnFailReq = return_fail_response
        self.htmlParse = html_parse

        self.session = requests.Session()
        self.headers.update({const.PARAM_USER_AGENT: self.ua})
        self.proxies = proxies

    def setParams(self, **kwargs) -> None:
        """设置请求参数"""
        if const.PARAM_TIMEOUT in kwargs:
            self.timeout = kwargs.get(const.PARAM_TIMEOUT)
        if const.PARAM_HEADERS in kwargs:
            self.headers = kwargs.get(const.PARAM_HEADERS)
        if const.PARAM_USER_AGENT in kwargs:
            self.ua = kwargs.get(const.PARAM_USER_AGENT)
            self.headers.update({const.PARAM_USER_AGENT: self.ua})
        if const.PARAM_REPEAT in kwargs:
            self.repeat = kwargs.get(const.PARAM_REPEAT)
        if const.DEFAULT_PARAM_RETURN_FAIL_RESPONSE in kwargs:
            self.returnFailReq = kwargs.get(const.DEFAULT_PARAM_RETURN_FAIL_RESPONSE)
        if const.PARAM_PROXIES in kwargs:
            self.proxies = kwargs.get(const.PARAM_PROXIES)

    def set_proxies(self, ip: str, port: Union[str, int]) -> None:
        """设置代理"""
        proxy_dict = {
            "http": "http://{}:{}".format(ip, port),
            "https": "https://{}:{}".format(ip, port)
        }
        self.proxies = proxy_dict

    def get_req_params(self) -> dict:
        """ 返回 requests 的请求参数"""
        params = {
            const.PARAM_HEADERS: self.headers,
            const.PARAM_TIMEOUT: self.timeout
        }
        if self.proxies is not None:
            params[const.PARAM_PROXIES] = self.proxies
        return params
