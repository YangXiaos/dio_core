# @Time         : 18-3-13 下午9:35
# @Author       : DioMryang
# @File         : DateTimeUtil.py
# @Description  : 时间工具类函数
from datetime import datetime as dt

from DioCore.Utils import Consts


patterns = [
    "%Y-%m-%dT%H:%M:%S"
]


def getStandardDatetime(datetime):
    """
    获取标准14位格式时间字符串
    :param datetime: 时间类子例
    :return:
    """
    return datetime.strftime(Consts.standardDateTimeFormat)


def getCurrentDatetime():
    """
    返回 当前时间 datetime对象
    :return: {datetime}
    """
    return dt.now()


def getCurStandardDate():
    """
    获取 当前标准时间 datetime
    :param datetime: {datetime} 当前时间对象
    :return: {string} 14位标准字符串
    """
    return getStandardDatetime(getCurrentDatetime())


def getStandardDate(date=None):
    """
    get standard datetime String
    :param date:
    :return:
    """
    if date is None:
        return getCurStandardDate()
    elif isinstance(date, dt):
        return getStandardDatetime(date)


def guess(dateTimeString: str) -> dt:
    for pattern in patterns:
        try:
            return dt.strptime(dateTimeString, pattern)
        except Exception as ignored:
            pass


if __name__ == '__main__':
    print(getStandardDate())
