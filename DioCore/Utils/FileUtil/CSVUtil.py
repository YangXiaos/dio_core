# @Time         : 18-6-17 下午9:09
# @Author       : DioMryang
# @File         : CsvUtil.py
# @Description  :
import csv
from typing import List, Iterable, Dict, Union


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


def save2csvV2(filePath: str, data: list=Iterable):
    """
    保存至 csv
    :param filePath: 文件路径
    :param data: 可迭代类型数据
    :return:
    """
    with open(filePath, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        headers = list(data[0].keys())
        writer.writerow(headers)

        for datum in data:
            rows = []
            for header in headers:
                if header not in datum:
                    rows.append("")
                elif isinstance(datum[header], dict) or isinstance(datum[header], list):
                    rows.append(str(datum[header]))
                else:
                    rows.append(datum[header])
            writer.writerow(rows)


def save2csvV3(filePath: str, data: Union[dict,list], fields: Iterable=None):
    """
    追加至csv
    :param filePath: 文件路径
    :param data: 数据
    :param fields:
    :return:
    """
    with open(filePath, 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        if isinstance(data, dict):
            writer.writerow([data[field] if field in data else "" for field in fields])
        elif isinstance(data, list):
            writer.writerow(data)


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
        headersLen = 0
        for ind, line in enumerate(list(csv.reader(csvfile))):
            lineLen = len(line)

            if ind == 0:
                headers = line
                headersLen = len(headers)
            else:
                if headersLen == lineLen:
                    csvDictList.append({keyName: line[ind] for ind, keyName in enumerate(headers)})
        return csvDictList
