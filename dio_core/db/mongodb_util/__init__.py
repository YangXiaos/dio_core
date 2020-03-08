# @Time         : 18-5-14 下午11:53
# @Author       : DioMryang
# @File         : const.py.py
# @Description  :
from pymongo import MongoClient


def create_connection(config=None):
    """
    创建mongodb 连接
    :param config:
    :return:
    """
    return MongoClient(**config) if config is not None else MongoClient()
