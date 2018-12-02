# @Time         : 18-11-27 下午10:09
# @Author       : DioMryang
# @File         : TextUtil.py
# @Description  :
import re


def getFirstMatch(text, pattern):
    match = re.match(pattern, text)
    return match.group(1) if match is not None else None
