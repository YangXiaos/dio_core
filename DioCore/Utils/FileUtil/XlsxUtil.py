# @Time         : 18-6-17 下午9:09
# @Author       : DioMryang
# @File         : XlsxUtil.py
# @Description  :
from typing import List

import openpyxl


def writeRows2Xlsx(filePath, data=None):
    """
    以 xlsx 形式写入
    :param filePath:
    :param data:
    :return:
    """
    wb = openpyxl.Workbook()
    ws = wb.active

    for ind, row in enumerate(data):
        for indChild, ele in enumerate(row):
            ws.cell(row=ind + 1, column=indChild + 1).value = ele
    wb.save(filePath)


def getRowsFromXlsx(file_name: str) -> List[str]:
    """获取"""
    excel = openpyxl.load_workbook(filename=file_name)
    for row in excel.active.iter_rows():
        yield list(map(lambda field: field.internal_value, row))


def python2xlsx(rows: List[dict], file_path: str, fields: List):
    """python对象 格式 2 xlxs"""
    wb = openpyxl.Workbook()
    ws = wb.active

    for row in rows:
        try:
            ws.append([row.get(field, "") for field in fields])
        except Exception as e:
            print(row.__str__() + "write fail")
    wb.save(file_path)
    wb.close()

if __name__ == '__main__':
    # writeRows2Xlsx("xx.xlsx", [[1,2,3], [1,2,3]])
    print(list(getRowsFromXlsx("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/FileUtil/xx.xlsx")))
