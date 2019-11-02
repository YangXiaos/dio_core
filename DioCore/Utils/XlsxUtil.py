import traceback

import openpyxl


def save2Xlsx(filePath, rows):
    """"""
    wb = openpyxl.Workbook()
    ws = wb.active

    for row in rows:
        try:
            ws.append(row)
        except Exception as e:
            print(row)
            print(e)
            traceback.print_exc()
    wb.save(filePath)
    wb.close()
