# @Time         : 18-7-7 下午6:30
# @Author       : DioMryang
# @File         : redis_client.py
from redis import Redis
from typing import Mapping, Iterable

from dio_core.db.redis_util import create_connection


class RedisClient(object):
    """
    RedisDao 键名封装
    """
    fn_names = []

    def __init__(self, conn: Redis, key_name: str):
        """
        :param conn: redis 连接
        :param conn: key_name 键名
        """
        self.conn = conn
        self.key_name = key_name

        for fnName in self.fn_names:
            def get_fn():
                fn1 = getattr(self.conn, fnName)

                def fn(*args, **kwargs):
                    return fn1(self.key_name, *args, **kwargs)
                return fn

            setattr(self, fnName, get_fn())

    def __del__(self):
        pass


class Key(RedisClient):
    """
    key 类型
    """
    fn_names = ["get", "del", "exists", "set", "incr", "decr"]


class Hash(RedisClient):
    """
    Hash 类型
    """
    fn_names = ["hdel", "hexists", "hset", "hgetall", "hkeys", "hlen", "hset", "hget", "hmset", "hvals"]

    def hdel(self, key_name: str):
        pass

    def hexists(self, key_name: str) -> bool:
        pass

    def hset(self, key_name: str, value: str):
        pass

    def hgetall(self) -> dict:
        pass

    def hkeys(self) -> Iterable[str]:
        pass

    def hlen(self) -> int:
        pass

    def hget(self, key_name: str) -> str:
        pass

    def hmset(self, mapping: Mapping[str, str]):
        pass

    def hvals(self) -> Iterable[str]:
        pass


class List(RedisClient):
    """
    List 类型
    """
    fn_names = ["blpop", "brpop", "brpoplpush", "lindex", "linsert", "llen", "lpop", "lpush", "lpushx", "lrange", "lrem",
               "lset", "ltrim", "rpop", "rpop", "lpush", "rpush", "rpushx", "sort"]

    def blpop(self):
        pass


class Set(RedisClient):
    """
    Set 类型
    """
    fn_names = ["sadd", "scard", "sdiff", "sdiffstore", "sinter", "sinterstore", "sismember", "smembers", "smove", "spop",
               "srandmember", "srem", "sunion", "sunionstore"]


if __name__ == '__main__':
    conn_ = create_connection()
    h = Hash(conn_, "dioddd")
    h.hset("bid", "va")
    print(h.hget("bid"))
