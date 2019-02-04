import re


def get_host(url: str) -> str:
    """获取 host"""
    pattern = "https?://(www\.)?(.*?)/"
    mc = re.match(pattern, url)
    return mc.groups()[1]