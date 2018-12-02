from DioCore.Network.Downloader import Downloader
from DioCore.Utils import TextUtil


def test_getFirstMatch():
    res = Downloader.getWithBs4("https://www.zhipin.com/job_detail/3265d372b1182c951HR50t2-ElU~.html")
    print(TextUtil.getFirstMatch(res.text, "job_id: '(.*?)',"))
