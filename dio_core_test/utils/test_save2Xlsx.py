from dio_core.utils import xlsx_util
from dio_core.utils.file_util import csv_util


def test_save2Xlsx():
    file_name = "/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/HUAWEI.SEARCH.csv"
    rows = csv_util.get_rows_from_csv(file_name)
    xlsx_util.save2Xlsx(file_name.replace("csv", "xlsx"), rows)
