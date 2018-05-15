# @Time         : 18-1-20 下午1:56
# @Author       : DioMryang
# @File         : Downloader.py
# @Description  :
import requests
from bs4 import BeautifulSoup

from DioCore import Consts
from DioCore.Downloader.Error import StateCodeException


def uaDecorator(fuc):
    """
    请求参数 默认装饰器
    :param fuc:
    :return:
    """
    def __fuc(*args, **kwargs):
        reqKwargs = kwargs.get("reqKwargs")
        if reqKwargs is not None:
            if "headers" not in reqKwargs:
                reqKwargs.update({"headers": Consts.HEADERS})
            if "timeout" not in reqKwargs:
                reqKwargs.update({"timeout": Consts.TIMEOUT})
        if "successStateCode" not in kwargs:
            kwargs.update({"successStateCode": Consts.SUCCESS_STATE_CODE})
        if "parser" not in kwargs:
            kwargs.update({"parser": Consts.PARSER})
        return fuc(*args, **kwargs)
    return __fuc


class Downloader(object):

    @staticmethod
    @uaDecorator
    def getRes(url, session=None, reqKwargs=None, **kwargs):
        """
        通过会话请求链接, 返回响应结果
        :param url: 请求 url
        :param session: 请求会话
        :param reqKwargs: 请求参数
        :return: 响应结果
        """
        reqKwargs = {} if reqKwargs is None else reqKwargs
        res = session.get(url, **reqKwargs) if session is not None else requests.get(url, **reqKwargs)

        code = kwargs.get("successStateCode")
        # 状态码错误
        if Downloader.__checkCode(code, res):
            raise StateCodeException("状态码异常 {}".format(res.status_code))

        return res

    @staticmethod
    def getJson(url, session=None, reqKwargs=None, **kwargs):
        """
        请求， 获取json形式的数据
        :param args: 列表参数
        :param reqKwargs: 请求参数
        :return: 请求结果， json形式数据
        """
        res = Downloader.getRes(url, session, reqKwargs, **kwargs)
        return res, res.json()

    @staticmethod
    def getSoup(url, session=None, reqKwargs=None, **kwargs):
        """
        获取解析soup
        :param args:
        :param kwargs:
        :return:
        """
        res = Downloader.getRes(url, session, reqKwargs, **kwargs)
        return res, BeautifulSoup(res.text, kwargs.get("parser"))

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

    @staticmethod
    def __checkCode(successStateCode, res):
        """
        校验code 是否正确
        :param stateCode: 状态码
        :param res: 响应结果
        :return:
        """
        return successStateCode != 0 and res.status_code != successStateCode

    def __init__(self, timeout=Consts.TIMEOUT, repty=Consts.REPTY_TIME, ua=Consts.UA, headers=Consts.HEADERS,
                 downloadType=Consts.DownloaderType.Res, successStateCode=Consts.SUCCESS_STATE_CODE, parser=Consts.PARSER):
        self.session = requests.Session()
        self.ua = ua
        self.headers = headers
        self.timeout = timeout
        self.headers.update({"User-Agent": ua})
        self.repty = repty
        self.downloadType = downloadType
        self.successStateCode = successStateCode
        self.parser = parser

        self.reqKwargs = {
            "timeout": self.timeout,
            "headers": self.headers,
        }
        self.otherKwargs = {
            "successStateCode": self.successStateCode,
            "parser": self.parser
        }

    def get(self, url, downloadType=Consts.DownloaderType.Res):
        reqFun = getattr(self, downloadType.value)
        for _ in range(self.repty):
            try:
                return reqFun(url, self.session, self.reqKwargs, self.otherKwargs)
            except Exception as e:
                print(e)

    def resetSession(self):
        """
        重新设置 session
        :return:
        """
        self.session = requests.Session()


if __name__ == '__main__':
    session_ = requests.Session()
    d = Downloader()
    res = d.getRes("http://blog.jobbole.com/112233/")

    res_ = Downloader.getRes("http://blog.csdn.net/u014756517/article/details/51953420")
    print(res_.text)
