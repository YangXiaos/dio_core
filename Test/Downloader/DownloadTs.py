# @Time         : 18-5-17 下午10:39
# @Author       : DioMryang
# @File         : DownloadTs.py
# @Description  :
from DioCore.Downloader import Downloader


def save(path, content):
    with open(path, 'wb') as f:
        for chunk in content:
            if chunk:
                f.write(chunk)
                f.flush()


format_url = [
    "https://hls-hw.xvideos-cdn.com/videos/hls/5b/0f/86/5b0f86f2ebe9863b040fd2c0024b2640/hls-1080p{}.ts?e=1526672592&l=0&h=77c6fb57e21cac53c1a4d1be155ea54b"
              ]

mv = 24
for url in format_url:
    for i in range(2, 200):
        print("打印")
        try:
            res, content, file_name, suffix = Downloader.getFile(url.format(i))
        except:
            break
        save(str(mv) + ":::" + str(i) + ".ts", res.iter_content(2048))
    mv += 1

