from DioCore.Utils import TextUtil
from DioCore.Utils.FileUtil import CSVUtil


csv = CSVUtil.getDictFromCsv("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/changshuai_test_miaomiao_20190602131823_853_8.item.csv")

for row in csv:
    itemId = TextUtil.getFirstMatch(row["full_url"], "dp/(.*?)/") or TextUtil.getFirstMatch(row["full_url"], "%2Fdp%2F(.*?)%2Fref%3")
    row["item_id"] = itemId


CSVUtil.save2csvV2("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/changshuai_test_miaomiao_20190602131823_853_8.item.temp.csv", csv)

print()