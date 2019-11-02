from DioCore.Utils.FileUtil import CSVUtil


def test_getDictFromCsv():
    rows = CSVUtil.getDictFromCsv("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/HUAWEI.SEARCH.csv")
    fields = "is_main_post	keyword	top_parent_twitter_id	tweet_id	url	screen_name	display_name	content	review_count	repost_count	like_count	publish_date	update_date".split("\t")
    data = []
    data.append(fields)
    for row in rows:
        data.append([row[field] for field in fields])

    CSVUtil.save2csv("/home/changshuai/PycharmProjects/dio_core/DioCore/Utils/teg/HUAWEI.SEARCH.v2.csv", data)


test_getDictFromCsv()