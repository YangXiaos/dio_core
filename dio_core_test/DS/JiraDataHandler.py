from dio_core.utils import json_util
from dio_core.utils.file_util import csv_util

jiraData = json_util.get_python_from_file("/home/changshuai/PycharmProjects/dio_core/output/jira.v2.json")


csv_util.save2csv_v2("/home/changshuai/PycharmProjects/dio_core/output/jira.v4.csv", jiraData)


pass