from dio_core.utils import xlsx_util
from dio_core.utils.file_util import csv_util


csv2 = csv_util.get_dict_from_csv("/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/面膜笔记_changshuai_20190711.csv")
xlsx_util.save2Xlsx("/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/面膜笔记_changshuai_20190711.xlsx", csv2)
