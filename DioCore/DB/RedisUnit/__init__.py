# @Time         : 18-5-17 下午9:08
# @Author       : DioMryang
# @File         : __init__.py.py
# @Description  :
import redis


def createConnect(host='localhost', port=6379):
    return redis.ConnectionPool(host=host, port=port)
