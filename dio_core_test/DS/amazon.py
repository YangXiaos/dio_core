from collections import defaultdict

from dio_core.utils.file_util import csv_util


def miao():
    mapping = defaultdict(int)
    item_csv = csv_util.get_dict_from_csv("/home/changshuai/Temp/item_amazon.csv")
    cmt_csv = csv_util.get_dict_from_csv("/home/changshuai/Temp/comment_amazon.v5.csv")

    for cmt in cmt_csv:
        mapping[cmt["parent_id"]] += 1

    for item in item_csv:
        if item["review_count"] != mapping[item["item_id"]]:
            print("{}\t{}\t{}\t{}\t{}".format(item["item_id"], item["review_count"], mapping[item["item_id"]],
                                          mapping[item["item_id"]]/int(item["review_count"]) if item["review_count"] != "0" else None
            ,int(item["review_count"]) - mapping[item["item_id"]]))


    print(mapping)

if __name__ == '__main__':
    miao()