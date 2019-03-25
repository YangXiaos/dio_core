from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities

from DioCore.Utils import FileUtil, DateTimeUtil, UrlUtil


def get_phantomjs(host="", port="", ua="", proxy_type="http", **kwargs):
    """
    获取webdriver
    :return:
    """
    if host and port:
        service_args = [
            "--proxy={}:{}".format(host, port),
            "--proxy-type={}".format(proxy_type),
            '--ignore-ssl-errors=true',
        ]
    else:
        service_args = []
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    if not ua:
        dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWeb"
                                             "Kit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36")
    else:
        dcap["phantomjs.page.settings.userAgent"] = ua
    driver = webdriver.PhantomJS(executable_path="/opt/package/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",
                                 service_args=service_args, desired_capabilities=dcap)
    return driver


def get_chrome(executable_path="/opt/driver/chromedriver",
               host="",
               port="",
               proxy_type="http",
               ua="", **kwargs):
    """
    获取webdriver
    :return:
    """
    chromeOptions = webdriver.ChromeOptions()
    if host and port:
        chromeOptions.add_argument('--proxy-server={}://{}:{}'.format(proxy_type, host, port))
        chromeOptions.add_argument('--proxy-type={}'.format(proxy_type))
    if ua:
        chromeOptions.add_argument("--user-agent=\"{}\"".format(ua))

    driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chromeOptions)
    return driver


if __name__ == '__main__':

    base_kwargs = {
        "executable_path": "/opt/driver/chromedriver"
    }
    company_kwargs = base_kwargs.copy()

    # 代理设置
    company_kwargs.update({"host": "127.0.0.1", "port": "1080", "proxy_type": "socks5", "proxy_platform": "company"})
    # company_kwargs.update({"host": "116.31.102.3", "port": "57000", "proxy_type": "http", "proxy_platform": "teg57000"})
    # company_kwargs.update({"host": "116.31.102.3", "port": "57002", "proxy_type": "http", "proxy_platform": "teg57002"})

    # company_kwargs.update({"ua": Const.SAFARI_UA, "ua_name": "safari"})
    # company_kwargs.update({"ua": Const.OPERA_UA, "ua_name": "opera"})
    # company_kwargs.update({"ua": Const.FIREFOX_UA, "ua_name": "firefox"})
    # company_kwargs.update({"ua": Const.TAO_BAO_UA, "ua_name": "taobao"})
    # company_kwargs.update({"ua_name": "chrome_max","ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"})
    company_kwargs.update({"ua_name": "chrome"})


    class Base(object):
        dir_path = "/home/changshuai/PycharmProjects/dio_core/Test/Data/{}"

    class Info(Base):
        url = ("https://www.google.com.hk/search?q=基因编辑&hl=zh-hk&tbs=cdr:1,cd_min:1/11/2019,cd_max:1/28/2019&tbm=nws"
               "&start=0&num=100")
        word = "基因编辑"


    class Info2(Base):
        url = ("https://www.google.com.hk/search?q=英国脱欧&hl=zh-hk&tbs=cdr:1,cd_min:1/10/2019,cd_max:1/19/2019&tbm=nws"
               "&start=0&num=100")
        word = "英国脱欧"


    class Info3(Base):
        url = ("https://www.google.com.hk/search?q=经贸磋商&hl=zh-hk&tbs=cdr:1,cd_min:1/21/2019,cd_max:1/28/2019&tbm=nws"
               "&start=0&num=100")
        word = "经贸磋商"

    class Info4(Base):
        url = ("https://www.google.com.hk/search?q=%E4%B9%9D%E4%BA%8C%E5%85%B1%E8%AF%86&tbs=cdr:1,cd_min:12/12/2018,cd_"
               "max:3/12/2019&tbm=nws&num=100&hl=zh-tw")
        word = "九二共识"

    class Info5(Base):
        url = ("https://www.google.com.hk/search?q=%e4%b8%ad%e5%85%b1+%e4%b8%a4%e4%bc%9a+%e4%b8%a4%e5%b2%b8&tbs=cdr:1,cd_min:12/12/2018,cd_"
               "max:3/12/2019&tbm=nws&num=100&hl=zh-tw")
        word = "中共 两会 两岸"

    class Info6(Base):
        url = ("https://www.google.com.tw/search?q=九二共识&tbs=cdr:1,cd_min:12/12/2018,cd_"
               "max:3/12/2019&tbm=nws&num=100&hl=zh-tw")
        word = "九二共识"

    class Info7(Base):
        url = ("https://www.google.com.hk/search?q=习五点&tbs=cdr:1,cd_min:12/12/2018,cd_"
               "max:3/12/2019&tbm=nws&num=100&hl=zh-tw")
        word = "习五点"

    class Info8(Base):
        url = ("https://www.google.com.tw/search?tbs=cdr:1,cd_min:3/6/2019,cd_max:3/20/2019&tbm=nws&q=%E4%B8%AD%E5%85%B1+%E4%B8%A4%E5%B2%B8+%E4%B8%A4%E4%BC%9A&num=100&hl=zh-tw")
        word = "中共 两岸 两会"

    class Info9(Base):
        url = ("https://www.google.com.tw/search?tbs=cdr%3A1%2Ccd_min%3A3%2F6%2F2019%2Ccd_max%3A3%2F20%2F2019&tbm=nws&q=%E4%B9%A0%E4%BA%94%E7%82%B9&num=100&hl=zh-tw")
        word = "习五点"

    class Info10(Base):
        url = ("https://www.google.com.tw/search?tbs=cdr%3A1%2Ccd_min%3A3%2F6%2F2019%2Ccd_max%3A3%2F20%2F2019&tbm=nws&q=%E4%B8%AD%E5%85%B1+%E4%B8%A4%E5%B2%B8++%E4%B8%A4%E4%BC%9A&num=100&hl=zh-tw")
        word = "中共 两岸 两会(2)"

    class Info11(Base):
        url = ("https://www.google.com.tw/search?tbs=cdr%3A1%2Ccd_min%3A3%2F6%2F2019%2Ccd_max%3A3%2F20%2F2019&tbm=nws&q="
               "%E4%B9%9D%E4%BA%8C%E5%85%B1%E8%AF%86&num=100&hl=zh-tw")
        word = "九二共识"

    def main():
        urls = [Info11]

        for info in urls:
            print("-------------{}".format(info.word))
            driver = None

            results = []
            try:
                driver = get_chrome(**company_kwargs)

                driver.get(info.url)
                while True:
                    soup = BeautifulSoup(driver.page_source, "lxml")
                    for tag in soup.select(".l.lLrAF,.card-section > a.RTNUJf"):
                        results.append(tag["href"])

                    for tag in soup.select(".g h3 > a, .g tr td > a"):
                        if "www.google.com" in tag["href"]:
                            results.append(UrlUtil.getUrlParams(tag["href"])["q"])

                    try:
                        element = driver.find_elements_by_link_text("下一頁")
                    except NoSuchElementException:
                        element = []

                    if element:
                        element[0].click()
                    else:
                        break

                prefix = ".".join([info.word,
                                   DateTimeUtil.getCurStandardDate()[4: 12],
                                   company_kwargs["ua_name"],
                                   company_kwargs["proxy_platform"]])
                file_name = "{}.txt".format(prefix)
                file_path = info.dir_path.format(file_name)
                print("写入file path: " + file_path)
                FileUtil.saveRows(file_path, data=results)
            except Exception as e:
                print(e)
            finally:
                if driver is not None:
                    driver.close()
                    driver.quit()
    main()
