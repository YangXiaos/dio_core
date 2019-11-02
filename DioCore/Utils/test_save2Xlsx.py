from DioCore.Utils import XlsxUtil
from DioCore.Utils.FileUtil import CSVUtil


def test_save2Xlsx():
    fileName = "/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/HUAWEI.SEARCH.csv"
    rows = CSVUtil.getRowsFromCsv(fileName)
    XlsxUtil.save2Xlsx(fileName.replace("csv", "xlsx"), rows)
