# @Time         : 18-6-17 下午9:09
# @Author       : DioMryang
# @File         : CsvUtil.py
# @Description  :
import csv
from typing import List, Iterable, Dict, Union


def save2csv(file_path: str, data: list = Iterable):
    """
    保存至 csv
    :param file_path: 文件路径
    :param data: 可迭代类型数据
    :return:
    """
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(data)


def save2csv_v2(file_path: str, data: list = Iterable):
    """
    保存至 csv
    :param file_path: 文件路径
    :param data: 可迭代类型数据
    :return:
    """
    with open(file_path, 'w', newline='') as file:
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


def save2csv_v3(file_path: str, data: Union[dict, list], fields: Iterable = None):
    """
    追加至csv
    :param file_path: 文件路径
    :param data: 数据
    :param fields:
    :return:
    """
    with open(file_path, 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        if isinstance(data, dict):
            writer.writerow([data[field] if field in data else "" for field in fields])
        elif isinstance(data, list):
            writer.writerow(data)


def get_rows_from_csv(file_path: str) -> List:
    """从csv文件 获取列表数据"""
    with open(file_path, "r", encoding="utf-8") as csv_file:
        # 读取csv文件，返回的是迭代类型
        result = []
        for line in csv.reader(csv_file):
            result.append(line)
        return result


def get_dict_from_csv(file_path: str) -> List[Dict]:
    """从csv文件 获取字典类型数据 """
    with open(file_path, "r", encoding="utf-8") as csv_file:
        headers = []
        csv_dict_list = []
        headers_len = 0
        for ind, line in enumerate(list(csv.reader(csv_file))):
            line_len = len(line)

            if ind == 0:
                headers = line
                headers_len = len(headers)
            else:
                if headers_len == line_len:
                    csv_dict_list.append({key_name: line[ind] for ind, key_name in enumerate(headers)})
        return csv_dict_list
