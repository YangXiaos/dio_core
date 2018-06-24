# @Time         : 18-6-17 下午9:09
# @Author       : DioMryang
# @File         : XlsxUnit.py
# @Description  :
from openpyxl import Workbook


def writeRowsXlsx(data=None, filePath=""):
    """
    以xlxs 形式写入
    :param data:
    :param filePath:
    :return:
    """
    wb = Workbook()
    ws = wb.active

    i = 1
    for row in data:
        j = 1
        for ele in row:
            ws.cell(row=i, column=j).value = ele
            j += 1
        i += 1

    wb.save(filePath)


if __name__ == '__main__':
    writeRowsXlsx([[1,2,3], [1,2,3]], "xx.xlsx")
