from dio_core.utils import file_util
from dio_core_test.utils import text_util

rows = text_util.get_all_match("\"(http.*)\"", file_util.readText("/home/changshuai/PycharmProjects/dio_core/Test/Data/temp.txt"))
# rows = TextUtil.get_all_match("htt.*", file_util.readText("/home/changshuai/PycharmProjects/dio_core/Test/Data/temp.txt"))

# file_util.saveRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/teg.190508/复仇者联盟4票房（无痕浏览器配置、高级选项）_changshuai_190508.txt", rows)
file_util.saveRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/伊朗核协议(网页)_changshuai_190508.txt", rows)

# file_util.saveRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/teg.190508/特朗普关税（无痕浏览器配置、高级选项）_heyou_190508.txt", rows)

