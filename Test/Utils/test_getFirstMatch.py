from DioCore.Utils import TextUtil


def test_getFirstMatch():
    print(TextUtil.getFirstMatch("http://co.com", "http://(.*)"))
