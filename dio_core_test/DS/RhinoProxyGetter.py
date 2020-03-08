from dio_core.network.downloader import Downloader


soup = Downloader.get_with_bs4("http://proxy.datastory.com.cn/getADAllHost?id=rhino").soup
for ip in soup.ipserver.select("ip"):
    print("http\t{}\t{}".format(ip.select_one("host").text, ip.select_one("port").text))