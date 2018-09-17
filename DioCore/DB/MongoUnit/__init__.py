# @Time         : 18-5-14 下午11:53
# @Author       : DioMryang
# @File         : Const.py.py
# @Description  :
from pymongo import MongoClient


def createConnect(config=None):
    """
    创建mongodb 连接
    :param config:
    :return:
    """
    return MongoClient(**config) if config is not None else MongoClient()
