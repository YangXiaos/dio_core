from typing import List

import pymysql

from DioCore.Utils import JsonUtil
from DioTest.DS.DBUtil import SSH


def printTable(appIds):
    with SSH() as server:
        selectTable(appIds)


def selectTable(appIds: List[int]):
    conn = pymysql.connect("127.0.0.1",
                           "rhino",
                           "rhino",
                           "db_datatub_rhino_v3",
                           port=5555, cursorclass=pymysql.cursors.DictCursor, charset='utf8')

    querySql = "SELECT t.* FROM t_rhino_task_config t " \
               "WHERE id in (" \
               "SELECT task_id_list FROM t_rhino_app_config WHERE app_id in ({})" \
               ");".format(",".join(map(str, appIds)))
    cur = conn.cursor()
    cur.execute(querySql)

    result = cur.fetchall()

    path = set()

    # 查看table
    for row in result:
        taskId = row["id"]
        print("任务Id: {}".format(taskId))

        distributeParam = JsonUtil.toPython(row["distribute_param"])
        for name, rule in distributeParam.items():
            if isinstance(rule, list):
                for _ in rule:
                    if "1" in _["writer"]:
                        path.add("{}".format( _["writer"]["1"]))
            else:
                if rule["id"] == 1 or rule["id"] == "1":
                    path.add("{}".format(rule["path"]))

    print(path)

printTable([10225])
