from DioCore.Utils import TextUtil


def test_getFirstMatch():
    print(TextUtil.getFirstMatch("job_id: '3265d372b1182c951HR50t2-ElU~',", "job_id: '(.*?)',"))
