# @Time         : 18-6-17 下午9:08
# @Author       : DioMryang
# @File         : Const.py.py
# @Description  : 文件工具类
from typing import List, Iterator


def readRows(file_name: str=None) -> Iterator:
    """
    读取行数
    :param file_name: 文件
    :return:
    """
    with open(file_name) as file:
        return map(lambda _: _.strip(), file.readlines())


def save(file_name: str="", data: str="") -> None:
    """
    写入文件
    :param file_name: 文件名
    :param data: 字符串数据
    :return:
    """
    with open(file_name, "w") as f:
        f.write(data)


def saveRows(file_name: str="", data: List=None) -> None:
    """
    保存数据行
    :param file_name: 文件名
    :param data: 数据
    :return:
    """
    with open(file_name, "w") as f:
        for row in data:
            f.write(row + "\r\n")


def readText(fileName: str=None) -> str:
    """
    读取文本
    :param fileName:
    :return:
    """
    with open(fileName) as file:
        return file.read()


if __name__ == '__main__':
    readText("/home/changshuai/PycharmProjects/dio_core/Test/Data/temp.txt")