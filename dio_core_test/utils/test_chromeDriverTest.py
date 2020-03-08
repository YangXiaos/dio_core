from unittest import TestCase

from dio_core.utils.webdriver_util import ChromeDriverTest


with ChromeDriverTest() as driver:
    driver.get("https://k.autohome.com.cn/detail/view_01d3zp9qbj68t36d1k6rwg0000.html")
    driver


