from typing import Union, Dict

from requests import Response

from DioCore.Network.Downloader import Setting


class MiddleWare(object):
    """请求 middleWare 控制输入输出"""
    def before(self, url: str, data: Union[str, Dict], setting: Setting):
        pass

    def after(self, url: str, data: Union[str, Dict], setting: Setting, res: Response):
        pass
