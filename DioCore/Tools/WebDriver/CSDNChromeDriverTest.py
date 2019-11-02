import time

from DioCore.Tools.WebDriver.ChromeDriverTool import ChromeDriver


with ChromeDriver(proxy={"host": "127.0.0.1", "port": "1088"}) as driver:
    driver.get("https://passport.csdn.net/login?code=public")
    driver.find_element_by_link_text("免密登录").click()
    time.sleep(2)
    driver.click("#tabOne")
    driver.send("#all", "13727504102")
    driver.send("#password-number", "676592ccyok")
    time.sleep(2)
    driver.find_element_by_css_selector('[data-type="account"]').click()

    time.sleep(2)
