# @Time         : 18-5-17 下午9:08
# @Author       : DioMryang
# @File         : Const.py.py
# @Description  :
import redis


def createConnect(host='localhost', port=6379, decode_responses=True):
    """
    create redis connection
    :param decode_responses:
    :param host:
    :param port:
    :return:
    """
    return redis.Redis(connection_pool=redis.ConnectionPool(host=host, port=port, decode_responses=decode_responses))


if __name__ == '__main__':
    conn = createConnect()

    conn.set("name", "value")