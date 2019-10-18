# @Time         : 18-1-20 下午1:56
# @Author       : DioMryang
# @File         : Downloader.py
# @Description  :
import traceback
from typing import Union, List, Dict

import chardet
import requests
from bs4 import BeautifulSoup
from requests import Response, Session

from DioCore.Network.Downloader import Setting, MiddleWare
from DioCore.Network.Downloader.Error import StateCodeException
from DioCore.Utils import LoggerUtil


class Downloader(object):
    PARSER = "lxml"
    logger = None

    def __new__(cls, *args, **kwargs):
        if cls.logger is None:
            cls.logger = LoggerUtil.getLogger(cls.__class__.__name__)
        return super().__new__(cls)

    def request(self, url: str, data: Union[str, Dict]=None, setting: Setting=None, session: Session=None, middleWares=None) -> Response:
        middleWares = middleWares if middleWares is not None else self.middleWares
        setting = setting if setting is not None else self.setting
        session = session if session is not None else self.session

        self.logger.info("[{}] 请求 {}".format(setting.request, url))
        # 失败重复请求
        for i in range(setting.repeat):
            try:
                for middleWare in middleWares:
                    middleWare.before(url, data, setting)

                # 请求url
                res = session.request(setting.request, url, data=data, **setting.getReqParams())

                for middleWare in middleWares:
                    middleWare.after(url, data, setting, res)

                # 请求code判定
                if setting.returnFailReq or res.status_code != 200:
                    raise StateCodeException("error code {}".format(res.status_code))

                # 解析页面
                if setting.htmlParse:
                    res.encoding = chardet.detect(res.content)["encoding"]
                    res.soup = BeautifulSoup(res.text, self.PARSER)
                    res.setting = setting

                return res
            except Exception as ignored:
                self.logger.error("第{}次 请求失败".format(i + 1))
                traceback.print_exc()

    def get(self, url: str) -> Response:
        """
        get 请求
        :param url: 请求 url
        :return: 响应结果
        """
        self.setting.request = Setting.GET
        return self.request(url)

    def post(self, url: str, data: Union[str, Dict]) -> Response:
        """
        通过会话请求链接, 返回响应结果
        :param data: 请求数据
        :param setting: 配置
        :param url: 请求 url
        :return: 响应结果
        """
        self.setting.request = Setting.POST
        return self.request(url, data)

    def getWithBs4(self, url: str) -> Response:
        self.setting.request = Setting.GET
        self.setting.htmlParse = True
        return self.get(url)

    def getBs4(self, url: str) -> BeautifulSoup:
        return self.getWithBs4(url).soup

    def getJson(self, url: str, data: Union[str, Dict]=None) -> Dict:
        if data is not None:
            self.setting.request = Setting.POST
            return self.request(url, data).json()
        else:
            self.setting.request = Setting.GET
            return self.request(url).json()

    def getFile(self, url, session=None, reqKwargs=None, **kwargs):
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

    def payload(self, url, data: str="") -> Response:
        """
        payload 请求
        :param url: 请求url
        :param data: 数据
        :param setting: 请求配置
        :return:
        """
        self.setting.request = Setting.POST
        return self.request(url, data)

    def __init__(self, setting: Setting=None, session: Session=None, middleWares: List[MiddleWare]=None):
        self.setting = setting if setting is not None else Setting()
        self.session = session if session is not None else requests.Session()
        self.middleWares = middleWares if middleWares is not None else []

    def resetSession(self):
        """
        重新设置 session
        :return:
        """
        self.session = requests.Session()


if __name__ == '__main__':
    setting_ = Setting()
    setting_.ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    downloader = Downloader(setting=setting_)
    res_ = downloader.request("http://www.landchina.com/DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx?wmguid=20aae8dc-4a0c-4af5-aedf-cc153eb6efdf&recorderguid=JYXT_ZJGG_9134&sitePath=")
    print(res_.text)
    pass