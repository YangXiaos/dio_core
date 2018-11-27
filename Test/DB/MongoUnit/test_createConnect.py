# @Time         : 18-8-11 下午2:53
# @Author       : DioMryang
# @File         : test_createConnect.py
from unittest import TestCase


# @Description  :
from DioCore.DB.MongoUnit import createConnect


class TestCreateConnect(TestCase):
    def test_createConnect(self):
        config = {
            "host": "localhost",
            "port": 27017,

        }
        conn = createConnect(config)

        # 获取数据库
        dio = conn.dio

        # 获取集合
        person = dio.person
        # person.insert_one({"_id": 1, "name": "杨小帅"})
        print(person.find_one(dict(_id=1)))