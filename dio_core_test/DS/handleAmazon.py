from dio_core_test.utils import text_util
from dio_core.utils.file_util import csv_util


csv = csv_util.get_dict_from_csv("/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/changshuai_test_miaomiao_20190602131823_853_8.item.csv")

for row in csv:
    itemId = text_util.get_first_match(row["full_url"], "dp/(.*?)/") or text_util.get_first_match(row["full_url"], "%2Fdp%2F(.*?)%2Fref%3")
    row["item_id"] = itemId


csv_util.save2csv_v2("/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/changshuai_test_miaomiao_20190602131823_853_8.item.temp.csv", csv)

print()