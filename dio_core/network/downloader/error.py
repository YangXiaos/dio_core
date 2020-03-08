# @Time         : 18-1-26 下午11:55
# @Author       : DioMryang
# @File         : error.py
# @Description  :


class StateCodeException(Exception):
    """
    状态码异常
    """
    pass


class RequestFailException(Exception):
    """
    请求失败
    """
    pass
