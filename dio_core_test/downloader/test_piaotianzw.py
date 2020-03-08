import re

import chardet

from dio_core.network.downloader import Downloader

def test():

    res = Downloader.get("https://www.piaotianzw.com/book/64763/index.html")
    res.encoding = chardet.detect(res.content)["encoding"]

    result = re.findall('class="dccss"><a href=[\'|"](.*?)[\'|"]>(.*?)</a>', res.text)
    print(result)
