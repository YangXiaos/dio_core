import hashlib


def md5(text: str):
    return hashlib.md5( text.encode(encoding='UTF-8')).hexdigest()