# @Time         : 18-11-27 下午10:18
# @Author       : DioMryang
# @File         : SystemConst.py
# @Description  :

# 返回失败请求
PARAM_RETURN_FAIL_RESPONSE = "returnFailResponse"

# 超时
PARAM_TIMEOUT = "timeout"

# 浏览器头
PARAM_HEADERS = "headers"

# user-agent
PARAM_USER_AGENT = "userAgent"

# proxies
PARAM_PROXIES = "proxies"

# 重复次数
PARAM_REPEAT = "repeat"

# user-agent
KEY_HEADER_USER_AGENT = "User-Agent"


# 浏览器头
DEFAULT_HEADER_USER_AGENT = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58"
                             ".0.3029.110 Safari/537.36")
DEFAULT_PARAM_TIMEOUT = 30
DEFAULT_REPEAT = 3
DEFAULT_PARAM_RETURN_FAIL_RESPONSE = False

DEFAULT_HEADERS = {
    KEY_HEADER_USER_AGENT: DEFAULT_HEADER_USER_AGENT
}

TAO_BAO_UA = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowse"
              "r/2.0 Safari/536.11")

OPERA_UA = "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"

FIREFOX_UA = ("Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3."
              "6.10")

SAFARI_UA = ("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.13"
             "3 Safari/534.16")
