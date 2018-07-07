# @Time         : 18-6-28 下午9:08
# @Author       : DioMryang
# @File         : ThreadUnit.py
# @Description  :
import threading


def getCurrentThreadName():
    """
    获取当前线程名
    :return:
    """
    return threading.current_thread().getName()