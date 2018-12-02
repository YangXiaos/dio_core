# @Time         : 18-7-7 下午6:30
# @Author       : DioMryang
# @File         : RedisClient.py
from redis import Redis
from typing import Mapping, Iterable

from DioCore.DB.RedisUtil import createConnect


class RedisClient(object):
    """
    RedisDao 键名封装
    """
    fnNames = []

    def __init__(self, conn: Redis, keyName: str):
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

    def __del__(self):
        pass


class Key(RedisClient):
    """
    key 类型
    """
    fnNames = ["get", "del", "exists", "set", "incr", "decr"]


class Hash(RedisClient):
    """
    Hash 类型
    """
    fnNames = ["hdel", "hexists", "hset", "hgetall", "hkeys", "hlen", "hset", "hget", "hmset", "hvals"]

    def hdel(self, keyName: str):
        pass

    def hexists(self, keyName: str) -> bool:
        pass

    def hset(self, keyName: str, value: str):
        pass

    def hgetall(self) -> dict:
        pass

    def hkeys(self) -> Iterable[str]:
        pass

    def hlen(self) -> int:
        pass

    def hget(self, keyName: str) -> str:
        pass

    def hmset(self, mapping: Mapping[str, str]):
        pass

    def hvals(self) -> Iterable[str]:
        pass


class List(RedisClient):
    """
    List 类型
    """
    fnNames = ["blpop", "brpop", "brpoplpush", "lindex", "linsert", "llen", "lpop", "lpush", "lpushx", "lrange", "lrem",
               "lset", "ltrim", "rpop", "rpop", "lpush", "rpush", "rpushx", "sort"]

    def miao(self):
        pass


class Set(RedisClient):
    """
    Set 类型
    """
    fnNames = ["sadd", "scard", "sdiff", "sdiffstore", "sinter", "sinterstore", "sismember", "smembers", "smove", "spop",
               "srandmember", "srem", "sunion", "sunionstore"]


if __name__ == '__main__':
    conn_ = createConnect()
    h = Hash(conn_, "dioddd")
    h.hset("bid", "va")
    print(h.hget("bid"))
