import pickle
import random
import time

from selenium.webdriver import ActionChains

from dio_core.tools.webdriver.ChromeDriverTool import ChromeDriver


def crawlShopList(autoLogin=True):
    with ChromeDriver(ua="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36") as driver:
        driver.request("http://h5.waimai.meituan.com/login?force=true&back_url=http%3A%2F%2Fh5.waimai.meituan.com%2Fwaimai%2Fmindex%2Fhome")

        if autoLogin:
            driver.set_window_size(320, 1080)
            driver.send("#phoneNumInput", "13727504102")
            driver.tap("#sendCodeBtn")
            code = input("输入验证码")
            driver.send("#codeInput", code)
            driver.tap("#iloginBtn")
            pickle.dump(driver.get_cookies(), open('cookies.pickle', 'wb'))
        else:
            driver.set_window_size(320, 1080)
            for cookie in pickle.load(open('cookies.pickle', 'rb')):
                driver.add_cookie(cookie)
            driver.request("http://h5.waimai.meituan.com/")
        # 设置详细地址
        driver.click("#wm-container > div > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1)")
        driver.click("#wm-container > div > div:nth-of-type(1) > div > div:nth-of-type(1) > div:nth-of-type(1) > div")
        driver.send('form  input[type="search"]', "广州")
        driver.click("#wm-container > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2) > ul > li")
        driver.send('form  input[type="search"]', "广州")
        driver.click("ul > li:nth-of-type(1)")

        # driver.tap("#wm-container > div > div > div:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(1) > ul > li:nth-of-type(3)")
        # driver.tap("li:nth-of-type(3)")

        # 采集逻辑
        while True:
            try:
                driver.execute_js("window.scrollBy(0, -100);")
                driver.execute_js("window.scrollBy(0, 500);")
                driver.logger.info("滚动抓取 {}".format(len(driver.find_elements_by_css_selector("#wm-container > div > div > div:nth-of-type(5) > div > ul > li"))))
                time.sleep(4)
            except Exception as e:
                pass

            if "已无更多商户" in driver.find_element_by_css_selector("#wm-container > div > div > div:nth-of-type(5) > div > div").text:
                break


def crawlShop(shopIds: [int]):
    with ChromeDriver(proxy={"host": "127.0.0.1", "port": "1088"},
                          ua="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36") as driver:
        driver.get("http://h5.waimai.meituan.com/")
        time.sleep(4)
        for cookie in pickle.load(open('cookies.pickle', 'rb')):
            driver.add_cookie(cookie)

        for shopId in shopIds:
            driver.request("http://h5.waimai.meituan.com/waimai/mindex/menu?dpShopId=&mtShopId={}".format(shopId))

            # 点击评论
            driver.click("nav div:nth-of-type(2)")
            i = 0
            while i < 5:
                driver.logger.info("[{}]评论 -> 滚动抓取数量 -> {}".format(shopId, len(driver.find_elements_by_css_selector("ul li"))))
                driver.scroll(0, 800)
                i += 1

            driver.logger.info("[{}]评论抓取结束".format(shopId))


def getMeiTuanCookie():
    with ChromeDriver(ua="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36") as driver:
        driver.get("http://h5.waimai.meituan.com/login?force=true&back_url=http%3A%2F%2Fh5.waimai.meituan.com%2Fwaimai%2Fmindex%2Fhome")
        time.sleep(2)

        driver.set_window_size(320, 1080)
        driver.send("#phoneNumInput", "13727504102")
        driver.tap("#sendCodeBtn")
        code = input("输入验证码")
        driver.send("#codeInput", code)
        driver.tap("#iloginBtn")
        time.sleep(5)
        pickle.dump(driver.get_cookies(), open('cookies.pickle', 'wb'))


def dio_testv2():
    with ChromeDriver(
        driver_path=r"C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe",
        proxy={"host": "127.0.0.1", "port": "8082"}
    ) as driver:
        driver.get("https://shop58803518.taobao.com/")
        driver.click()

        print()


def dio_testv3():
    # email = "hjgkxsyjmxs@gmail.com"
    # help_email = "yujxusizhd@gmail.com"
    # password = "Zyl@123456"
    new_password = "Zyl@123456"

    def modify(email, help_email, password):
        with ChromeDriver(
                driver_path=r"C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe",
                # proxy={"host": "127.0.0.1", "port": ""},
        ) as driver:

            # 登陆设置
            driver.request(("https://accounts.google.com/signin/v2/identifier?hl=zh-TW&continue=https%3A%2F%2Fwww.google.co"
                            "m.hk%2F%3Fpli%3D1&flowName=GlifWebSignIn&flowEntry=AddSession"))
            driver.send("#identifierId", email)
            driver.click("#identifierNext")
            driver.send('[type="password"]', password)
            driver.click("#passwordNext")

            try:
                driver.click("form section > div ul > li:nth-of-type(1) > div")
                driver.send('[type="email"]', help_email)
                driver.click('[id="view_container"] > div > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div:nth-of-type(1) > div')
            except:
                pass

            # 设置中文
            driver.request("https://myaccount.google.com/language?utm_source=google-account&utm_medium=web")
            driver.click('#i3 > div > div.N9Ni5 > div')
            driver.send('[type="text"][jsname="YPqjbf"]', "简体中文")
            driver.click('[role="listbox"] > [role="option"][tabindex="0"]')
            driver.click("[aria-label=\"简体中文\"]")
            driver.click('[data-is-adaptive="true"] > div:nth-of-type(3) > [role="button"]:nth-of-type(2)')

            # 重设密码
            driver.request("https://myaccount.google.com/personal-info")
            driver.click("[href=\"signinoptions/password?utm_source=google-account&utm_medium=web&continue=https%3A%2F%2Fmyaccount.google.com%2Fpersonal-info\"]")
            driver.send("[id=\"Passwd\"]", password)
            driver.click("[id=\"signIn\"]")
            driver.find_elements_by_css_selector('[type="password"]')[0].send_keys(new_password)
            driver.find_elements_by_css_selector('[type="password"]')[1].send_keys(new_password)
            time.sleep(2)
            driver.click('body > c-wiz > div > div:nth-of-type(3) > c-wiz > div > div:nth-of-type(3) > div:nth-of-type(2) > div')

            # 设置安全性
            driver.request("https://myaccount.google.com/security")
            driver.click('[href="lesssecureapps?utm_source=google-account&utm_medium=web"]')
            driver.click('[role="checkbox"]')

            # 开启 pop/
            driver.request("https://mail.google.com/")
            driver.click('[href="?&v=prg"]')
            driver.click('[href="?v=prfap"]')
            driver.click('#bx_pe_3', time_load=1)
            driver.click('#bx_ie_1', time_load=1)
            driver.click('[name="nvp_a_prefs"]')

    for _ in [
        # ("fghjrtyucvbn876444@gmail.com", "berthawooster041@yahoo.com", "76t5resdyu87",),
        # ("jhmnbvghjkuy09876444@gmail.com", "hakesdrema86@yahoo.com", "y6trdyhu8",),
        ("ytresdfgbvcxjhg876444@gmail.com", "bolgermarva0@yahoo.com", new_password,), # 异常
        # ("hgfdfghytrertyiu9876444@gmail.com", "gallupbrigida27@yahoo.com", "t5r4edtyu87y6",),
        # ("cvbnjhgfcvbnjh9876444@gmail.com", "lashawndaa303@yahoo.com", "6t5redyu7y6",),
    ]:

        try:
            modify(*_)
        except:
            print(_[0], "修改异常")


def dio_testV4():
    moblie = "5635386548"

    def get_track(distance):
        track = []
        current = 0
        mid = distance * 3 / 4
        t = 0.2
        v = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0 + a * t
            move = v0 * t + 1 / 2 * a * t * t
            current += move
            track.append(round(move))
        return track

    with ChromeDriver(
            driver_path=r"C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe",
            proxy={"host": "127.0.0.1", "port": "1071"},
    ) as driver:
        driver.request("https://world.taobao.com/markets/all/sea/register")
        # driver.click("#J_AgreementBtn")
        driver.switch_to_frame("J_Member")
        slide = driver.find_element_by_css_selector(".nc_iconfont.btn_slide")
        ActionChains(driver).click_and_hold(slide).perform()
        X = 0
        tracks = get_track(300)
        for x in tracks:
            start = time.time()
            ActionChains(driver).move_by_offset(xoffset=x, yoffset=0).perform()
            end = time.time()
            print("execute {:.2f}".format(start - end))
        time.sleep(0.5)
        ActionChains(driver).release().perform()

        # driver.drag_and_drop(".nc_iconfont.btn_slide", x=300)
        driver.send("#J_Mobile", moblie)
        try:
            driver.click(".tb-select-dropdown.tb-select-dropdown.tb-menu-button-dropdown.tb-button-dropdown")
            driver.find_element_by_css_selector("#ks-component6898").click()
        except:
            pass
        try:
            driver.click(".tb-select-dropdown.tb-select-dropdown.tb-menu-button-dropdown.tb-button-dropdown")
            driver.find_element_by_css_selector("#ks-component6898").click()
        except:
            pass
        # driver.click("#J_Agreement")
        driver.click("#J_BtnMobileForm")


if __name__ == '__main__':
    # getMeiTuanCookie()
    # crawlShop([925682604406362, 945594072818124, 993521612857161, 1004241851218447, 887427330694403, 999839509715220,
    #            915031085534771, 1087392418037875, 883012104317199, 859518633222585, 992834418101280, 978824234759567,
    #            1048767777174164, 1033082556635958, 908691713778483, 931313306561056, 896545546250041, 1090029527998846,
    #            896571316086698, 911715370767321])
    dio_testV4()
