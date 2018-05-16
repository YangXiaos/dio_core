# @Time         : 18-5-14 下午11:53
# @Author       : DioMryang
# @File         : __init__.py.py
# @Description  :
from pymongo import MongoClient


def createMongodbConnect(config=None):
    """
    创建mongodb 连接
    :param config:
    :return:
    """
    return MongoClient(**config) if config is not None else MongoClient()


def insertData(data, conn=None, dbName=None, collectionName=None, db=None, collection=None):
    """
    插入数据
    :param data:
    :param collectionName:
    :param db:
    :param collection:
    :return:
    """
    if collection:
        collection.insert(data)
    elif collectionName and db:
        db[collectionName].insert(data)
    elif conn and dbName and collectionName:
        conn[dbName][collectionName].insert(data)
    raise ValueError("conn or dbName or collectionName or db or collection cant be None")
