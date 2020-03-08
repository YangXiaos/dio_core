# Author: YangXiaoShuai
# Date: 2020/2/28 10:49
# Project / File: dio_core : xiaohulu_test 
# Desc: google 测试
from dio_core.tools.webdriver import ChromeDriver


def test_chrome_driver():
    with ChromeDriver(driver_path=r"E:\Framework\chrome_driver\chromedriver_win32\chromedriver.exe",
                      proxy={"host": "127.0.0.1", "port": "1080"}) as driver:
        driver.get("www.google.com")
        driver.implicitly_wait(60 * 1000)


if __name__ == '__main__':
    test_chrome_driver()
