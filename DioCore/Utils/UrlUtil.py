import re
from urllib import parse
from urllib.parse import ParseResult

from urllib3.util import Url


def get_host(url: str) -> str:
    """获取 host"""
    pattern = "https?://(www\.)?(.*?)/"
    mc = re.match(pattern, url)
    return mc.groups()[1]


def unquote(url: str) -> str:
    """url 编码"""
    return parse.quote(url, "utf-8")


def urlencode(query) -> str:
    """url 参数编码"""
    return parse.urlencode(query)


def getUrlParams(url) -> dict:
    query = parse.urlsplit(url).query
    params = parse.parse_qs(query)

    for key in params:
        params[key] = params[key][0]
    return params

if __name__ == '__main__':
    url = "https://www.google.com.hk/url?q=https://www.chinatimes.com/newspapers/20190226000160-260301&sa=u&ved=0ahukewjn7pbxxexgahvvijqihfaibyuqjqwipygcmay&usg=aovvaw11chnhjwbwnoowiwci1kvk://"
    params = getUrlParams(url)
    print(params)
    # url.
    # print(splitquery())