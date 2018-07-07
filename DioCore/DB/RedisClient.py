# @Time         : 18-7-7 下午6:30
# @Author       : DioMryang
# @File         : RedisClient.py
from DioCore.DB.RedisUnit import createConnect


class Redis(object):
    """
    Redis 键名封装
    """
    fnNames = []

    def __init__(self, conn, keyName):
        """
        :param conn: redis 连接
        :param conn: keyName 键名
        """
        self.conn = conn
        self.keyName = keyName

        for fnName in self.fnNames:
            def getFn():
                fn1 = getattr(self.conn, fnName)

                def fn(*args, **kwargs):
                    return fn1(self.keyName, *args, **kwargs)
                return fn

            setattr(self, fnName, getFn())


class Key(Redis):
    """
    key 类型
    """
    fnNames = ["get", "del", "exists", "set", "incr", "decr"]


class Hash(Redis):
    """
    Hash 类型
    """
    fnNames = ["hdel", "hexists", "hset", "hgetall", "hkeys", "hlen", "hset", "hget"]


class List(Redis):
    """
    List 类型
    """
    fnNames = ["blpop", "brpop", "brpoplpush", "lindex", "linsert", "llen", "lpop", "lpush", "lpushx", "lrange", "lrem",
               "lset", "ltrim", "rpop", "rpoplpush", "rpush", "rpushx", "sort"]


class Set(Redis):
    """
    Set 类型
    """
    fnNames = ["sadd", "scard", "sdiff", "sdiffstore", "sinter", "sinterstore", "sismember", "smembers", "smove", "spop"
               "srandmember", "srem", "sunion", "sunionstore"]


if __name__ == '__main__':
    conn_ = createConnect()
    h = Hash(conn_, "dioddd")
    h.hset("bid", "va")
    print(h.hget("bid"))
