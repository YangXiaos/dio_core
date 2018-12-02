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
DEFAULT_HEADER_USER_AGENT = ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029."
                     "110 Safari/537.36")
DEFAULT_PARAM_TIMEOUT = 30
DEFAULT_REPEAT = 3
DEFAULT_PARAM_RETURN_FAIL_RESPONSE = False

DEFAULT_HEADERS = {
    KEY_HEADER_USER_AGENT: DEFAULT_HEADER_USER_AGENT
}

