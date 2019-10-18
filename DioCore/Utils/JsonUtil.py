# @Time         : 18-6-4 下午10:25
# @Author       : DioMryang
# @File         : JsonUtil.py
# @Description  :
import json
from typing import Union


def toJson(obj):
    """
    python对象 生成json 格式字符串
    :param obj: 对象
    :return:
    """
    return json.dumps(obj,separators=(',', ':'), ensure_ascii=False)


def toPython(jsonString):
    """
    json字符串 生成json 对象
    :param jsonString:
    :return:
    """
    return json.loads(jsonString)


def getPythonFromFile(fileName: str) -> Union[dict, list]:
    """
    从文件获取 python 对象
    :param fileName: 文件名
    :return:
    """
    return json.load(open(fileName))


def dumpPython2File(python: dict, fileName: str):
    """
    保存 字符串到文件
    :param data: 字符串数据
    :return:
    """
    json.dump(python, open(fileName, "w"))
