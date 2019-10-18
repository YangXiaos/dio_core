# @Time         : 19-2-7 下午1:56
# @Author       : DioMryang
# @File         : ImageUtil.py
# @Description  :
from PIL import Image
from typing import Tuple


def resize(imgPath: str, size: Tuple, target: str=""):
    """图片 resize"""
    img = Image.open(imgPath)
    tmp = img.resize(size, Image.ANTIALIAS)
    img.close()
    tmp.save(target if target else imgPath)
