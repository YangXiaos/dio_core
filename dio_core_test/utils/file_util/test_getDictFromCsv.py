from dio_core.utils.file_util import csv_util


def test_get_dict_from_csv():
    rows = csv_util.get_dict_from_csv("/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/HUAWEI.SEARCH.csv")
    fields = "is_main_post	keyword	top_parent_twitter_id	tweet_id	url	screen_name	display_name	content	review_count	repost_count	like_count	publish_date	update_date".split("\t")
    data = []
    data.append(fields)
    for row in rows:
        data.append([row[field] for field in fields])

    csv_util.save2csv("/home/changshuai/PycharmProjects/dio_core/dio_core/utils/teg/HUAWEI.SEARCH.v2.csv", data)


test_get_dict_from_csv()