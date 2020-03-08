import traceback

import openpyxl


def save2Xlsx(file_path, rows):
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
    wb.save(file_path)
    wb.close()
