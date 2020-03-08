from typing import Union, Dict

from requests import Response

from dio_core.network.downloader import Setting


class MiddleWare(object):
    """请求 middleWare 控制输入输出"""
    def before(self, url: str, data: Union[str, Dict], setting: Setting):
        pass

    def after(self, url: str, data: Union[str, Dict], setting: Setting, res: Response):
        pass
