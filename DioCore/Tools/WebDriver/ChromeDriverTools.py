import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from DioCore.Utils import TimeUtil, LoggerUtil

DRIVER_PATH = "/opt/package/chromedriver"


def flow():
    driver = None
    try:
        # chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument("'--proxy-server={}".format("http://127.0.0.1:1080"))
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)

        driver.get("http://www.baidu.com")
        print()
        TimeUtil.sleep(15)
    except Exception as e:
        print(e)
    finally:
        if driver is not None:
            driver.close()
            driver.quit()


class ChromeDriver(object):
    def __init__(self, driverPath=DRIVER_PATH, proxy=None):

        chromeOptions = webdriver.ChromeOptions()
        if proxy is not None:
            chromeOptions.add_argument("--proxy-server={}".format("http://{}:{}".format(proxy["host"], proxy["port"])))

        self.driver = webdriver.Chrome(executable_path=driverPath, chrome_options=chromeOptions)
        self.logger = LoggerUtil.getLogger(ChromeDriver)


    def __enter__(self):
        self.logger.info("初始化 chrome driver")
        return self.driver

    def __exit__(self,exc_type,exc_value,traceback):
        self.driver.close()
        self.driver.quit()



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
