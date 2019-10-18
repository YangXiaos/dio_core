# @Time         : 18-11-27 下午10:09
# @Author       : DioMryang
# @File         : TextUtil.py
# @Description  :
import re


def getFirstMatch(text, pattern):
    """获取单个匹配"""
    match = re.search(pattern, text)
    return match.group(1) if match is not None else None


def getAllMatch(pattern: str, string: str):
    """获取所有匹配"""
    return re.findall(pattern, string)