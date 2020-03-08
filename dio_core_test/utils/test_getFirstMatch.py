from dio_core.network.downloader import Downloader
from dio_core_test.utils import text_util


def test_get_first_match():
    res = Downloader.get_with_bs4("https://www.zhipin.com/job_detail/3265d372b1182c951HR50t2-ElU~.html")
    print(text_util.get_first_match(res.text, "job_id: '(.*?)',"))
