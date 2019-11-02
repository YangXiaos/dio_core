from DioCore.Utils import XlsxUtil
from DioCore.Utils.FileUtil import CSVUtil


csv2 = CSVUtil.getDictFromCsv("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/面膜笔记_changshuai_20190711.csv")
XlsxUtil.save2Xlsx("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/面膜笔记_changshuai_20190711.xlsx", csv2)
