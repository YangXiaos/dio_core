import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from dio_core.tools.webdriver import USER_AGENT
from dio_core.utils import logger_util, time_util


class PhantomjsDriver(object):
    def __init__(self, proxy: dict = None, ua: str = USER_AGENT.DEFAULT_UA):
        self.logger = logger_util.get_logger(PhantomjsDriver)

        dcap = dict(DesiredCapabilities.PHANTOMJS)

        if proxy is not None:
            service_args = [
                "--proxy={}:{}".format(proxy["host"], proxy["port"]),
                "--proxy-type={}".format(proxy["type"]),
                '--ignore-ssl-errors=true',
            ]
        else:
            service_args = []

        if not ua:
            dcap["phantomjs.page.settings.userAgent"] = ua
        else:
            dcap["phantomjs.page.settings.userAgent"] = ua
        self.driver = webdriver.PhantomJS(executable_path="/opt/package/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",
                                          service_args=service_args, desired_capabilities=dcap)
        self.driver.logger = self.logger

    def __enter__(self):
        self.logger.info("初始化 chrome driver")
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    with PhantomjsDriver() as driver:
        #
        time_cost_list = []

        #
        for i in range(100):
            startDate = time_util.get_unix()
            driver.get("https://www.baidu.com/")
            endDate = time_util.get_unix()
            time_cost_list.append(endDate - startDate)
            driver.logger.info("耗时 {}".format(endDate - startDate))

        driver.logger.info("均值为 {}".format(sum(time_cost_list) / len(time_cost_list)))
        time.sleep(2)
