# @Time         : 18-6-4 下午10:25
# @Author       : DioMryang
# @File         : json_util.py
# @Description  :
import json
from typing import Union


def to_json(obj):
    """
    python对象 生成json 格式字符串
    :param obj: 对象
    :return:
    """
    return json.dumps(obj,separators=(',', ':'), ensure_ascii=False)


def to_python(json_string):
    """
    json字符串 生成json 对象
    :param json_string:
    :return:
    """
    return json.loads(json_string)


def get_python_from_file(file_name: str) -> Union[dict, list]:
    """
    从文件获取 python 对象
    :param file_name: 文件名
    :return:
    """
    return json.load(open(file_name))


def dump_python2_file(python: dict, file_name: str):
    """
    保存 字符串到文件
    :param file_name:
    :param python:
    :return:
    """
    json.dump(python, open(file_name, "w"))
