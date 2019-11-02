from collections import defaultdict

from DioCore.Utils.FileUtil import CSVUtil


def miao():
    mapping = defaultdict(int)
    item_csv = CSVUtil.getDictFromCsv("/home/changshuai/Temp/item_amazon.csv")
    cmt_csv = CSVUtil.getDictFromCsv("/home/changshuai/Temp/comment_amazon.v5.csv")

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