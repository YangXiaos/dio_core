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
    # "https://hls-hw.xvideos-cdn.com/videos/hls/11/1b/e3/111be3ad5e87ace4c961c54931dda270-1/hls-720p{}.ts?e=1530209393&l=0&h=75ffa9ccbf546145946c6b9ba9be9f3b"
    "https://hls2-l3.xvideos-cdn.com/a59835adbe3c1d6f1d57211d33de8957f379a278-1530210119/videos/hls/d4/d9/f4/d4d9f4aa376c53fff89eaf121d90378d/hls-720p{}.ts"
]

mv = 24
for url in format_url:
    for i in range(2, 200):
        try:
            print("打印")
            res, content, file_name, suffix = Downloader.getFile(url.format(i))
        except:
            print("fail")
            break
        save(str(mv) + ":::" + str(i) + ".ts", res.iter_content(2048))
    mv += 1

