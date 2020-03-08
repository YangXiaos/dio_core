import pymysql

from dio_core.utils import json_util
from dio_core.utils.logger_util import get_logger

logger = get_logger(__file__)


def getRhino() -> pymysql.Connection:
    """获取 rhino connect"""
    return pymysql.connect("devrhino1", "rhino", "rhino", "db_datatub_rhino", port=3306,
                           cursorclass=pymysql.cursors.DictCursor, charset='utf8')


def updateSourceCrawlId(taskId: int, mapping: dict):
    """
    更新
    mapping = {
       "redis-link": [1, 3]
    }
    """
    conn = getRhino()
    cur = conn.cursor()

    # 获取taskConfig
    querySql = "SELECT t.* FROM t_rhino_task_config t WHERE id = {};".format(taskId)
    logger.info(querySql)
    cur.execute(querySql)
    result = cur.fetchone()

    # 处理 distribute
    distributeParam = json_util.to_python(result["distribute_param"])
    for key, newCrawlerIds in mapping.items():
        if key in distributeParam:
            rules = distributeParam[key]["rules"]
            for ind, rule in enumerate(distributeParam[key]["rules"]):
                if rule.startswith("{sourceCrawlerId}#in#"):
                    crawlerIds = set(map(int, rule.replace("{sourceCrawlerId}#in#", "").split(",")))
                    crawlerIds = crawlerIds | set(newCrawlerIds)
                    crawlerIds = list(crawlerIds)
                    crawlerIds.sort()
                    rules[ind] = "{{sourceCrawlerId}}#in#{}".format(",".join(map(str, crawlerIds)))

    # 处理crawler_id_list
    crawlerIdList = result["crawler_id_list"]
    crawlerIdList = set(map(int, crawlerIdList.split(",")))
    for key, newCrawlerIds in mapping.items():
        crawlerIdList = crawlerIdList | set(newCrawlerIds)

    crawlerIdList = list(crawlerIdList)
    crawlerIdList.sort()

    # 更新sql
    distributeParamUpdate = json_util.to_json(distributeParam)
    crawlerIdListUpdate = ",".join(map(str, crawlerIdList))
    updateSql = "UPDATE t_rhino_task_config SET distribute_param = '{}', crawler_id_list = '{}' WHERE id = {} ".format(distributeParamUpdate, crawlerIdListUpdate, taskId)
    print(updateSql)
    cur.execute(updateSql)

    cur.close()
    conn.close()


if __name__ == '__main__':
    kwargs = {
        "taskId": 1003219,
        "mapping": {
            "redis-link": [4,5],
            "redis-items": [6],
            "hbase-items": [6],
            "hbase-cmt": [7],
        }
    }
# updateSourceCrawlId(1003219, {"redis-items": [999999999, 99999999]})
