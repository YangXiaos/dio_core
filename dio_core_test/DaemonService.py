import datetime
import time
from collections import Counter

from dio_core.network.downloader import Downloader
from dio_core.utils import send_email_util


class SMGCounter(object):

    # 最大发送次数, 时间间隔，日计数
    MAX_SEND_TIME = 50
    INTERVAL = datetime.timedelta(minutes=30)
    day_counter = Counter()

    # 手机列表
    PHONE_LIST = [
        "13727504102",
        "18520141655",
        "18648819990",
        "17771982161",
    ]

    # 发送消息
    def send_smg(self):
        pass


class DaemonService(object):
    """
    守护服务
    """
    lsv80 = "http://192.168.1.4"
    lsv81 = "http://192.168.1.4:81"
    osv5051 = "http://47.110.145.20:5051/"
    osv5052 = "http://47.110.145.20:5052/"

    counter = Counter()

    def start(self):
        while True:

            # 本地服务是否正常
            self.test_location_service(self.lsv80)
            self.test_location_service(self.lsv81)

            # 线上服务是否正常
            self.test_online_service(self.osv5051)
            self.test_online_service(self.osv5052)

            time.sleep(30)

    def test_location_service(self, request_url):
        try:
            res = Downloader().get(request_url)
            if res.json()["code"] == 200:
                print("{} 本地服务正常".format(request_url))
                self.counter[request_url] = 0
                return
            else:
                raise Exception("code 异常 {}".format(res.json()["code"]))
        except:
            self.counter[request_url] += 1
            if self.counter[request_url] >= 3:
                send_email_util.sendEmail("178069857@qq.com", "服务 {} 运行超过3次异常".format(request_url), subject="[淘宝Xsign服务异常] 线上服务异常")
            print("{} 接口服务异常".format(request_url))

            # 尝试重启下服务

    def test_online_service(self, request_url):
        try:
            res = Downloader().get(request_url)
            if res.json()["code"] == 200:
                print("{} 本地服务正常".format(request_url))
                self.counter[request_url] = 0
            else:
                raise Exception("code 异常 {}".format(res.json()["code"]))
        except:
            self.counter[request_url] += 1
            if self.counter[request_url] >= 3:
                send_email_util.sendEmail("178069857@qq.com", "服务 {} 运行超过3次异常".format(request_url), subject="[淘宝Xsign服务异常] 本地服务异常")
            print("{} 接口服务异常".format(request_url))


DaemonService().start()
