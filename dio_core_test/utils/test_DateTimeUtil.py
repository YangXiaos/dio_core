from dio_core.utils import datetime_util


def test_guess():
    print(datetime_util.get_standard_date(datetime_util.guess("2018-11-27T14:43:37")))