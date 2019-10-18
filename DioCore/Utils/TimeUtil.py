# @Time         : 18-6-30 下午3:24
# @Author       : DioMryang
# @File         : TimeUtil.py
# @Description  :

import time


def sleep(second):
    """
    暂停一段时间
    :param second: 秒数
    :return:
    """
    time.sleep(second)


def getUnix():
    return int(round(time.time() * 1000))


def getUnixV2():
    return int(round(time.time()))


currentMilliTime = lambda: int(round(time.time() * 1000))

if __name__ == '__main__':
    print(getUnixV2())
