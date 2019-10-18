from DioCore.Utils import DateTimeUtil


def test_guess():
    print(DateTimeUtil.getStandardDate(DateTimeUtil.guess("2018-11-27T14:43:37")))