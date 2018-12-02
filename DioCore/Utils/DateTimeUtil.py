# @Time         : 18-3-13 下午9:35
# @Author       : DioMryang
# @File         : DateTimeUtil.py
# @Description  : 时间工具类函数
from datetime import datetime as dt

from DioCore.Utils import Consts


class DateTimeUtil(object):
    """
    时间工具类函数


    """
    @staticmethod
    def getStandardDatetime(datetime):
        """
        获取标准14位格式时间字符串
        :param datetime: 时间类子例
        :return:
        """
        return datetime.strftime(Consts.standardDateTimeFormat)

    @staticmethod
    def getCurrentDatetime():
        """
        返回 当前时间 datetime对象
        :return: {datetime}
        """
        return dt.now()

    @staticmethod
    def getCurStandardDate():
        """
        获取 当前标准时间 datetime
        :param datetime: {datetime} 当前时间对象
        :return: {string} 14位标准字符串
        """
        return DateTimeUtil.getStandardDatetime(DateTimeUtil.getCurrentDatetime())

    @staticmethod
    def getStandardDate(date=None):
        """
        get standard datetime String
        :param date:
        :return:
        """
        if date is None:
            return DateTimeUtil.getCurStandardDate()
        elif isinstance(date, dt):
            return DateTimeUtil.getStandardDatetime(date)


if __name__ == '__main__':
    print(DateTimeUtil.getStandardDate())
