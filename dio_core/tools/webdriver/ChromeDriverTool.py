import time

from selenium import webdriver
from selenium.webdriver import TouchActions, ActionChains

from dio_core.tools.webdriver import USER_AGENT
from dio_core.utils import logger_util

DRIVER_PATH = "/opt/package/chromedriver"


class ChromeDriver(object):

    def __init__(self, driver_path: str = DRIVER_PATH, proxy: dict = None, ua: str = USER_AGENT.DEFAULT_UA,
                 headless: bool = False):

        chrome_options = webdriver.ChromeOptions()
        if proxy is not None:
            chrome_options.add_argument("--proxy-server={}".format("http://{}:{}".format(proxy["host"], proxy["port"])))
            chrome_options.add_argument("--ignore-certificate-errors")
        if ua:
            chrome_options.add_argument("user-agent=" + ua)
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
        self.driver.click = self.click
        self.driver.tap = self.tap
        self.driver.send = self.send_keys
        self.driver.execute_js = self.execute_js
        self.driver.flick = self.flick
        self.driver.scroll = self.scroll
        self.driver.request = self.request
        self.driver.drag_and_drop = self.drag_and_drop

        self.logger = logger_util.get_logger(ChromeDriver)
        self.driver.logger = self.logger

    def __enter__(self):
        self.logger.info("初始化 chrome driver")
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.close()
        self.driver.quit()

    # 模拟控制
    def click(self, css_selector, time_load=5):
        self.driver.find_element_by_css_selector(css_selector).click()
        time.sleep(time_load)

    def tap(self, css_selector, time_load=5):
        action = TouchActions(self.driver)
        action.tap(self.driver.find_element_by_css_selector(css_selector)).perform()
        time.sleep(time_load)

    def send_keys(self, css_selector, value, time_load=5):
        self.driver.find_element_by_css_selector(css_selector).send_keys(value)
        time.sleep(time_load)

    def execute_js(self, script, time_load=2):
        self.driver.execute_script(script)
        time.sleep(time_load)

    def flick(self, css_selector, x=0, y=0, speed=50, time_load=2):
        action = TouchActions(self.driver)
        action.flick_element(self.driver.find_element_by_css_selector(css_selector), x, y, speed).perform()
        time.sleep(time_load)

    def scroll(self, x=0, y=0):
        action = TouchActions(self.driver)
        action.scroll(xoffset=x, yoffset=y).perform()

    def request(self, url, time_load=3):
        self.logger.info("chrome driver 请求{}".format(url))
        self.driver.get(url)
        time.sleep(time_load)

    def drag_and_drop(self, css_selector, x=0, y=0, time_load=2):
        chains = ActionChains(self.driver)
        chains.click_and_hold(self.driver.find_element_by_css_selector(".nc_iconfont.btn_slide"))
        chains.drag_and_drop_by_offset(self.driver.find_element_by_css_selector(css_selector), x, y).perform()
        # chains.

        time.sleep(time_load)


if __name__ == '__main__':
    #
    # with ChromeDriver() as driver:
    #     driver.get("https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
    #     driver.find_element_by_css_selector("#TPL_username_1").send_keys("杨畅帅")
    #     driver.find_element_by_css_selector("#TPL_password_1").send_keys("676592ccyok")
    #
    #     driver.find_element_by_css_selector("#nc_1_n1z")
    #     ActionChains(driver).drag_and_drop_by_offset(driver.find_element_by_css_selector("#nc_1_n1z"), 298, 0).perform()

    info = "LaughingInfant38541	5036640260	mariamartin297@yahoo.com".split("\t")
    account = info[0] + "@gmail.com"
    telephone = info[1]
    email = info[2]
    password = "ds@12345678"

    with ChromeDriver(proxy={"host": "127.0.0.1", "port": "1081"}) as driver:
        driver.maximize_window()
        driver.get(
            "https://accounts.google.com/signin/v2/identifier?service=accountsettings&hl=zh-CN&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.find_element_by_css_selector("#identifierId").click()
        driver.find_element_by_css_selector("#identifierId").send_keys(account)
        driver.find_element_by_css_selector(".CwaK9").click()
        time.sleep(3)
        driver.find_element_by_css_selector("[jsname=\"YPqjbf\"]").send_keys("ds@12345678")
        driver.find_element_by_css_selector(".CwaK9").click()
        time.sleep(3)
        driver.find_element_by_css_selector(".INl6Jd").click()
        time.sleep(2)
        driver.find_element_by_css_selector("[jsname=\"YPqjbf\"]").send_keys(email)
        driver.find_element_by_css_selector(".CwaK9").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".CwaK9").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".n6Gm2e").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".CwaK9").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".CwaK9").click()
        time.sleep(2)
        driver.find_elements_by_link_text("Personal info")[0].click()
        time.sleep(2)
        driver.find_element_by_css_selector('[href="phone?utm_source=google-account&utm_medium=web"]').click()
        time.sleep(2)
        driver.find_element_by_css_selector('[jsname="jCPfkc"]').click()
        time.sleep(2)
        driver.find_element_by_css_selector('[href="https://www.google.com/voice?hl=en&authuser=0#phones"]').click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        driver.find_elements_by_css_selector('[aria-label="Messages: 3 unread"]')[1].click()
        time.sleep(1)
        msgSize = 0
        while True:
            if msgSize != len(driver.find_elements_by_css_selector('[gv-thread-id]')):
                msgSize = len(driver.find_elements_by_css_selector('[gv-thread-id]'))
                driver.find_elements_by_css_selector('[gv-thread-id]')[0].click()
            time.sleep(1)

    with ChromeDriver(headless=True) as driver:
        #
        time_cost_list = []

        #
        for i in range(100):
            startDate = TimeUtil.get_unix()
            driver.get("https://www.qq.com/")
            endDate = TimeUtil.get_unix()
            time_cost_list.append(endDate - startDate)
            driver.logger.info("耗时 {}".format(endDate - startDate))

        driver.logger.info("均值为 {}".format(sum(time_cost_list) / len(time_cost_list)))
        time.sleep(2)
