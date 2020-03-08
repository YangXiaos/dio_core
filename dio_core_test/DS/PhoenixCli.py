from dio_core.utils.teg.SSHUtil import ssh_execute
from DioTest.DS.DBUtil import DB


def insertHmeta(fields: list, tableName, isOnline: bool=False):
    """"""
    print("\n")
    desc = input("输入desc")
    print("\n")
    rowkeyRule = input("输入rowkey,eg({keyword}) :")
    print("\n")
    md5Length = input("md5_length,default 5:")
    print("\n")
    rowkeyPrefixRule = input("输入rowkey rule")

    fieldsList = ",".join(fields)

    sql = """
    insert into t_rhino_htable_meta (table_name,rowkey_rule,rowkey_prefix_rule,md5_length,field_list,`desc`)
    values (
        '{}',
        '{}',
        '{}',
        '{}',
        '{}'
    );""".format(tableName, rowkeyRule, rowkeyPrefixRule, md5Length, fieldsList, desc)
    print("执行sql {}".format(sql))

    # with db(isOnline) as db:
    #     db.cur.execute("")
    #     db.connection.commit()


def buildTable(fields):
    pass


if __name__ == '__main__':
    insertHmeta(
        ["jobName", "title", "keyword", "publish_date", "content", "image_url_list", "view_count"],
        "dt.rhino.app.yili_zongyi_post_v2"
    )