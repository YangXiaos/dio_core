from DioCore.Network.Downloader import Downloader
from DioCore.Network.Downloader.Downloader import Setting

s = Setting()
s.setProxies("116.31.102.3", "57000")
ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
ua = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11"

s.headers.update(
    {
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9",
        'upgrade-insecure-requests': "1",
        'user-agent': "\"{}\"".format(ua),
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'authority': "www.google.com.hk",
        'cache-control': "max-age=0",
        'referer': "https://www.google.com.hk/",
    }
)
res = Downloader.getWithBs4("https://www.google.com.hk/search?q=%E5%9F%BA%E5%9B%A0%E7%BC%96%E8%BE%91&hl=zh-hk&tbs=cdr:1,cd_min:1/11/2019,cd_max:1/28/2019&tbm=nws&start=0&num=100", setting=s)

results = []
for aTag in res.soup.select(".l.lLrAF, .card-section > a.RTNUJf"):
    print(aTag.attrs["href"])
