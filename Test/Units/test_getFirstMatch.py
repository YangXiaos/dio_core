from DioCore.Units import TextUnit


def test_getFirstMatch():
    print(TextUnit.getFirstMatch("http://co.com", "http://(.*)"))
