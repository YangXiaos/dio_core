from DioCore.Utils import TextUtil, FileUtil


rows = TextUtil.getAllMatch("\"(http.*)\"", FileUtil.readText("/home/changshuai/PycharmProjects/dio_core/Test/Data/temp.txt"))
# rows = TextUtil.getAllMatch("htt.*", FileUtil.readText("/home/changshuai/PycharmProjects/dio_core/Test/Data/temp.txt"))

# FileUtil.saveRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/teg.190508/复仇者联盟4票房（无痕浏览器配置、高级选项）_changshuai_190508.txt", rows)
FileUtil.saveRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/伊朗核协议(网页)_changshuai_190508.txt", rows)

# FileUtil.saveRows("/home/changshuai/PycharmProjects/dio_core/Test/Data/teg.190508/特朗普关税（无痕浏览器配置、高级选项）_heyou_190508.txt", rows)

