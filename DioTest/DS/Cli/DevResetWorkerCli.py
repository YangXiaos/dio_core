from DioCore.Network.Downloader import Downloader
from DioCore.Network.Downloader.Downloader import Setting
from DioCore.Utils import LoggerUtil, TimeUtil
from DioTest.DS.Cli.DevRestartCli import devRestart

CLOSE_WORKER_URL = "http://rhino.dev.datatub.com/api/supervisor/workerClose"
SELECT_WORKER_URL = "http://rhino.dev.datatub.com/api/monitor/clusterOverview"
ADD_WORKER_URL = "http://rhino.dev.datatub.com/api/supervisor/addWorker?num={}&workerGroup={}"
CLEAR_WORKER_URL = "http://rhino.dev.datatub.com/api/supervisor/clearDeadWorker"
LOGIN_URL = "http://rhino.dev.datatub.com/api/login/ajax/tryLogin"

LOG = LoggerUtil.getLogger(__file__)


def closeWorker(cookie, group="full"):
    """
    关闭 worker
    :return:
    """
    headers = {
        'Cookie': cookie,
        'Origin': "http://rhino.dev.datatub.com",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Accept': "*/*",
        'Referer': "http://rhino.dev.datatub.com/",
        'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive"
    }
    setting = Setting()
    setting.headers = headers
    setting.request = "POST"

    res = Downloader(setting=setting).payload(CLOSE_WORKER_URL, "workerGroup={}".format(group))
    LOG.info("CLOSE WORKER 结果 {}".format(res.json()))
    if res.json()["code"] == 0:
        return True


def selectWorker(cookie):
    """
    查询worker
    :return:
    """
    headers = {
        'Cookie': "{}".format(cookie),
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        'Host': "rhino.dev.datatub.com"
    }
    setting = Setting()
    setting.headers = headers
    json = Downloader(setting=setting).getJson(SELECT_WORKER_URL)
    LOG.log("SELECT 结果 {}".format(json))
    if json["code"] == 0:
        return True


def addWorker(workerNum, group, cookie):
    """
    添加 worker
    :return:
    """
    headers = {
        'Cookie': "{}".format(cookie),
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        'Host': "rhino.dev.datatub.com"
    }
    setting = Setting()
    setting.headers = headers
    json = Downloader(setting=setting).getJson(ADD_WORKER_URL.format(workerNum, group))
    LOG.info("ADD 结果 {}".format(json))
    if json["code"] == 0:
        return True


def clearWorker(cookie):
    headers = {
        'Cookie': "{}".format(cookie),
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        'Host': "rhino.dev.datatub.com"
    }
    setting = Setting()
    setting.headers = headers
    setting.request = "POST"
    res = Downloader(setting=setting).request(CLEAR_WORKER_URL)
    LOG.info("Clear 结果 {}".format(res.json()))
    if res.json()["code"] == 0:
        return True


def login():
    headers = {
        'Host': "rhino.dev.datatub.com",
        'Content-Length': "35",
        'Accept': "*/*",
        'Origin': "http://rhino.dev.datatub.com",
        'X-Requested-With': "XMLHttpRequest",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Referer': "http://rhino.dev.datatub.com/login.html",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "close"
    }

    payload = "userName=changshuai&passWord=123456"
    setting = Setting()
    setting.headers = headers
    setting.request = "POST"
    res = Downloader(setting=setting).payload(LOGIN_URL, payload)
    return res.cookies.get("JSESSIONID")


# ssh 执行 命令
# 关闭worker
# 查看worker 数至 0
#
if __name__ == '__main__':
    devRestart(group="full", branch="test")
    workerNum = 3
    group = "full"
    cookie = "JSESSIONID={}".format(login())

    closeWorker(cookie, group)
    TimeUtil.sleep(10)
    addWorker(workerNum, group, cookie)
    TimeUtil.sleep(60)
    clearWorker(cookie)
