# @Time         : 18-6-17 下午9:09
# @Author       : DioMryang
# @File         : CsvUtil.py
# @Description  :
import csv
from typing import List, Iterable, Dict


def save2csv(filePath: str, data: list=Iterable):
    """
    保存至 csv
    :param filePath: 文件路径
    :param data: 可迭代类型数据
    :return:
    """
    with open(filePath, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(data)


def getRowsFromCsv(filePath: str) -> List:
    """从csv文件 获取列表数据"""
    with open(filePath, "r", encoding="utf-8") as csvfile:
        # 读取csv文件，返回的是迭代类型
        result = []
        for line in csv.reader(csvfile):
            result.append(line)
        return result


def getDictFromCsv(filePath: str) -> List[Dict]:
    """从csv文件 获取字典类型数据 """
    with open(filePath, "r", encoding="utf-8") as csvfile:
        headers = []
        csvDictList = []

        for ind, line in enumerate(list(csv.reader(csvfile))):
            lineLen, headersLen = len(line), 0

            if ind == 0:
                headers = line
                headersLen = len(headers)
            else:
                if headersLen == lineLen:
                    csvDictList.append({keyName: line[ind] for ind, keyName in enumerate(headers)})
        return csvDictList
