from DioCore.Utils import JsonUtil
from DioCore.Utils.FileUtil import CSVUtil

jiraData = JsonUtil.getPythonFromFile("/home/changshuai/PycharmProjects/dio_core/output/jira.v2.json")


CSVUtil.save2csvV2("/home/changshuai/PycharmProjects/dio_core/output/jira.v4.csv", jiraData)


pass