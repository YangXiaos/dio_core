import time

from selenium import webdriver
from selenium.webdriver import TouchActions, ActionChains

from DioCore.Tools.WebDriver import USER_AGENT
from DioCore.Utils import TimeUtil, LoggerUtil

DRIVER_PATH = "/opt/package/chromedriver"


class ChromeDriver(object):

    def __init__(self, driverPath: str=DRIVER_PATH, proxy: dict=None, ua: str=USER_AGENT.DEFAULT_UA,
                 headless: bool=False):

        chromeOptions = webdriver.ChromeOptions()
        if proxy is not None:
            chromeOptions.add_argument("--proxy-server={}".format("http://{}:{}".format(proxy["host"], proxy["port"])))
            chromeOptions.add_argument("--ignore-certificate-errors")
        if ua:
            chromeOptions.add_argument("user-agent=" + ua)
        if headless:
            chromeOptions.add_argument("--headless")
            chromeOptions.add_argument("--disable-gpu")

        self.driver = webdriver.Chrome(executable_path=driverPath, chrome_options=chromeOptions)
        self.driver.click = self.click
        self.driver.tap = self.tap
        self.driver.send = self.sendKeys
        self.driver.executeJs = self.executeJs
        self.driver.flick = self.flick
        self.driver.scroll = self.scroll
        self.driver.request = self.request
        self.driver.drag_and_drop = self.drag_and_drop

        self.logger = LoggerUtil.getLogger(ChromeDriver)
        self.driver.logger = self.logger

    def __enter__(self):
        self.logger.info("初始化 chrome driver")
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.close()
        self.driver.quit()

    # 模拟控制
    def click(self, cssSelector, timeLoad=5):
        self.driver.find_element_by_css_selector(cssSelector).click()
        time.sleep(timeLoad)

    def tap(self, cssSelector, timeLoad=5):
        action = TouchActions(self.driver)
        action.tap(self.driver.find_element_by_css_selector(cssSelector)).perform()
        time.sleep(timeLoad)

    def sendKeys(self, cssSelector, value, timeLoad=5):
        self.driver.find_element_by_css_selector(cssSelector).send_keys(value)
        time.sleep(timeLoad)

    def executeJs(self, script, timeLoad=2):
        self.driver.execute_script(script)
        time.sleep(timeLoad)

    def flick(self, cssSelector, x=0, y=0, speed=50, timeLoad=2):
        Action = TouchActions(self.driver)
        Action.flick_element(self.driver.find_element_by_css_selector(cssSelector), x, y, speed).perform()
        time.sleep(timeLoad)

    def scroll(self, x=0, y=0):
        action = TouchActions(self.driver)
        action.scroll(xoffset=x, yoffset=y).perform()

    def request(self, url, timeLoad=3):
        self.logger.info("chrome driver 请求{}".format(url))
        self.driver.get(url)
        time.sleep(timeLoad)

    def drag_and_drop(self, cssSelector, x=0, y=0, timeLoad=2):
        chains = ActionChains(self.driver)
        chains.click_and_hold(self.driver.find_element_by_css_selector(".nc_iconfont.btn_slide"))
        chains.drag_and_drop_by_offset(self.driver.find_element_by_css_selector(cssSelector), x, y).perform()
        # chains.

        time.sleep(timeLoad)


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
        driver.get("https://accounts.google.com/signin/v2/identifier?service=accountsettings&hl=zh-CN&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
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
            startDate = TimeUtil.getUnix()
            driver.get("https://www.qq.com/")
            endDate = TimeUtil.getUnix()
            time_cost_list.append(endDate - startDate)
            driver.logger.info("耗时 {}".format(endDate - startDate))

        driver.logger.info("均值为 {}".format(sum(time_cost_list)/len(time_cost_list)))
        time.sleep(2)
