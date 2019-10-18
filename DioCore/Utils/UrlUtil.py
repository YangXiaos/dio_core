import re
from urllib import parse


def getHost(url: str) -> str:
    """获取 host"""
    pattern = "https?://(www\.)?(.*?)/"
    mc = re.match(pattern, url)
    return mc.groups()[1]


def unquote(url: str) -> str:
    """url 解码"""
    return parse.unquote(url, "utf-8")


def quote(url: str) -> str:
    """url 解码"""
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


def patchUrl(pathUrl: str) -> str:
    if pathUrl.startswith("//"):
        return "https:" + pathUrl


def unquotePostData(postData: str) -> dict:
    """ post数据 """
    post = {}
    for item in postData.split("&"):
        split_ = item.split("=")
        key = split_[0]
        if len(split_) == 1:
            post[key] = ""
        else:
            post[key] = parse.unquote(split_[1])
    return post


if __name__ == '__main__':
    url = "https://www.google.com.hk/url?q=https://www.chinatimes.com/newspapers/20190226000160-260301&sa=u&ved=0ahukewjn7pbxxexgahvvijqihfaibyuqjqwipygcmay&usg=aovvaw11chnhjwbwnoowiwci1kvk://"
    params = getUrlParams(url)
    print(params)
    # url.
    # print(splitquery())