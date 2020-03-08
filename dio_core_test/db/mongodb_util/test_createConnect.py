# @Time         : 18-8-11 下午2:53
# @Author       : DioMryang
# @File         : test_create_connection.py
from unittest import TestCase


# @Description  :
from dio_core.db.mongodb_util import create_connection


class Testcreate_connection(TestCase):
    def test_create_connection(self):
        config = {}
        conn = create_connection(config)

        # 获取数据库
        dio = conn.dio

        # 获取集合
        person = dio.person
        person.insert_one({"_id": 1, "name": "杨小帅"})
        # print(person.find_one(dict(_id=1)))
