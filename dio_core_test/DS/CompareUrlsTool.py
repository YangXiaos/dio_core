from dio_core.utils import file_util


def compareUrls(file_name1, file_name2, base_dir="/home/changshuai/PycharmProjects/dio_core/Test/Data/{}"):
    """
    比较Url
    :param base_dir:
    :param file_name1: url集1
    :param file_name2: url集2
    :return:
    """
    file_name1 = file_name1 if file_name1.startswith("/") else base_dir.format(file_name1)
    file_name2 = file_name2 if file_name2.startswith("/") else base_dir.format(file_name2)

    row1 = set(file_util.readRows(file_name1))
    row2 = set(file_util.readRows(file_name2))

    print("交集1: {}".format(len(row1)))
    print("交集2: {}".format(len(row2)))
    print("交集: {}".format(len(row1 & row2)))

    print(len(row1 & row2) / len(row1 | row2))


def getAccordance(file_name1: str, file_name2: str, base_dir="/home/changshuai/PycharmProjects/dio_core/Test/Data/{}"):
    """
    获取准确率
    :param base_dir:
    :param file_name1: 浏览器数据
    :param file_name2: 爬虫数据
    :return:
    """
    file_name1 = file_name1 if file_name1.startswith("/") else base_dir.format(file_name1)
    file_name2 = file_name2 if file_name2.startswith("/") else base_dir.format(file_name2)
    row1 = set(file_util.readRows(file_name1))
    row2 = set(file_util.readRows(file_name2))

    print("交集: {}".format(len(row1 & row2)))
    print(len(row1 & row2) / len(row1))

if __name__ == '__main__':
    # compareUrls("/home/changshuai/PycharmProjects/dio_core/Test/Data/基因编辑.03061155.taobao.company.txt", "/home/changshuai/PycharmProjects/dio_core/Test/Data/基因编辑.03061155.chrome_max.company.txt")
    # getAccordance("/home/changshuai/PycharmProjects/dio_core/Test/Data/92.location.txt", "/home/changshuai/PycharmProjects/dio_core/Test/Data/92.spiders.txt")
    # getAccordance(
    #     "/home/changshuai/PycharmProjects/dio_core/Test/Data/teg/复仇者联盟4_changshuai_web.txt",
    #     "/home/changshuai/PycharmProjects/dio_core/Test/Data/teg/复仇者联盟4_changshuai_crawler.txt")
    getAccordance(
        "/home/changshuai/PycharmProjects/dio_core/Test/Data/伊朗核协议(网页)_changshuai_190508.txt",
        "/home/changshuai/PycharmProjects/dio_core/Test/Data/伊朗核协议(爬虫)_changshuai_190508.txt")