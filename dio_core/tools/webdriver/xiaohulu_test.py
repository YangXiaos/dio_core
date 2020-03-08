# Author: YangXiaoShuai
# Date: 2020/2/28 10:49
# Project / File: dio_core : xiaohulu_test 
# Desc: 小葫芦单元测试
from dio_core.tools.webdriver.ChromeDriverTool import ChromeDriver


def test_chrome_driver():
    with ChromeDriver(driver_path=r"E:\Framework\chrome_driver\chromedriver_win32\chromedriver.exe", ) as driver:
        pass


if __name__ == '__main__':
    test_chrome_driver()
