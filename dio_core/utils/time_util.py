# @Time         : 18-6-30 下午3:24
# @Author       : DioMryang
# @File         : time_util.py
# @Description  :

import time


def sleep(second):
    """
    暂停一段时间
    :param second: 秒数
    :return:
    """
    time.sleep(second)


def get_unix():
    return int(round(time.time() * 1000))


def get_unix_v2():
    return int(round(time.time()))


current_milli_time = lambda: int(round(time.time() * 1000))

if __name__ == '__main__':
    print(get_unix_v2())
