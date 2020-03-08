import re
from urllib import parse


def get_host(url: str) -> str:
    """获取 host"""
    pattern = r"https?://(www\.)?(.*?)/"
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


def get_url_params(url) -> dict:
    query = parse.urlsplit(url).query
    params = parse.parse_qs(query)

    for key in params:
        params[key] = params[key][0]
    return params


def patch_url(path_url: str) -> str:
    if path_url.startswith("//"):
        return "https:" + path_url


def unquote_post_data(post_data: str) -> dict:
    """ post数据 """
    post = {}
    for item in post_data.split("&"):
        split_ = item.split("=")
        key = split_[0]
        if len(split_) == 1:
            post[key] = ""
        else:
            post[key] = parse.unquote(split_[1])
    return post


if __name__ == '__main__':
    _url = "https://www.google.com.hk/url?q=https://www.chinatimes.com/newspapers/20190226000160-260301&sa=u&ved=0ahukewjn7pbxxexgahvvijqihfaibyuqjqwipygcmay&usg=aovvaw11chnhjwbwnoowiwci1kvk://"
    _params = get_url_params(_url)
    print(_params)
    # url.
    # print(splitquery())