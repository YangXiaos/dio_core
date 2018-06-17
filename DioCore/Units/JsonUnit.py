# @Time         : 18-6-4 下午10:25
# @Author       : DioMryang
# @File         : JsonUnit.py
# @Description  :
import json


def toJson(obj):
    """
    python对象 生成json 格式字符串
    :param obj: 对象
    :return:
    """
    return json.dumps(obj)


def toPython(jsonString):
    """
    json字符串 生成json 对象
    :param jsonString:
    :return:
    """
    return json.loads(jsonString)
