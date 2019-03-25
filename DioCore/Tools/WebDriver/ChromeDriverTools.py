from selenium import webdriver

DRIVER_PATH = "/opt/package/chromedriver"


def flow():
    driver = None
    try:
        # chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_argument("'--proxy-server={}".format("http://127.0.0.1:1080"))
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, )

        driver.get("https://www.google.com/search?q=%E5%9F%BA%E5%9B%A0%E7%BC%96%E8%BE%91&hl=zh-TW&authuser=0&biw=1745&bih=829&source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F14%2F2019%2Ccd_max%3A1%2F28%2F2019&tbm=nws")
        print()
    except Exception as e:
        print(e)
    finally:
        if driver is not None:
            driver.close()
            driver.quit()

if __name__ == '__main__':
    flow()