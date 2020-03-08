import time

from dio_core.utils.webdriver_util import get_chrome


driver = None

try:
    print("喵喵喵喵")
    driver = get_chrome(host="127.0.0.1", port=1083)
    print("喵喵喵喵2")
    driver.get("https://www.dianping.com/search/keyword/2/0_%E5%8F%A4%E5%90%8D")
    time.sleep(3000)
    driver
except Exception as e:
    print(e)
finally:
    if driver is not None:
        driver.close()
        driver.quit()   