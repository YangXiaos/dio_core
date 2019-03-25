# @Time         : 18-3-13 下午9:35
# @Author       : DioMryang
# @File         : DateTimeUtil.py
# @Description  : 时间工具类函数
from datetime import datetime as datetime
from typing import Union


patterns = [
    "%Y-%m-%dT%H:%M:%S"
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y年%m月%d日 %H:%M:%S",
    "%Y年%m月%d日%H:%M",
    "%Y年%m月%d日",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d %h:%m:%s",
    "%Y-%m-%d",
    "%m-%d %H:%M",
    "%Y.%m.%d",
    "%Y年%m月%d日 %H时%M分%S秒",
    "%m月%d日 %H:%M",
    "%Y-%m-%d  %H:%M:%S"
]
STANDARD_DATETIME_FORMAT = "%Y%m%d%H%M%S"


def getStandardDatetime(dt: datetime) -> str:
    """获取标准14位格式时间字符串"""
    return dt.strftime(STANDARD_DATETIME_FORMAT)


def getCurrentDatetime() -> datetime:
    """返回 当前时间 datetime对象"""
    return datetime.now()


def getCurStandardDate() -> str:
    """获取 当前标准时间 datetime"""
    return getStandardDatetime(getCurrentDatetime())


def getStandardDate(dt: Union[datetime, None]=None):
    """get standard datetime String"""
    if dt is None:
        return getCurStandardDate()
    elif isinstance(dt, datetime):
        return getStandardDatetime(dt)


def guess(dateTimeString: str) -> Union[datetime, None]:
    for pattern in patterns:
        try:
            return datetime.strptime(dateTimeString, pattern)
        except Exception as ignored:
            pass
    return None


def toDatetime(string: str, pattern: str) -> datetime:
    """字符串 转化成datetime """
    return datetime.strptime(string, pattern)


def pretty(dt: Union[datetime, str]) -> str:
    """时间美化"""
    if isinstance(dt, str):
        return datetime.strptime(dt, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")
    else:
        return dt.strftime("%Y-%m-%d %H:%M:%S")



if __name__ == '__main__':
    print(getStandardDate()[4: 12])
