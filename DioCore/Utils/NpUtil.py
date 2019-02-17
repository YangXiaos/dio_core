# @Time         : 19-2-7 下午4:48
# @Author       : DioMryang
# @File         : NpUtil.py
# @Description  :
import numpy as np
from PIL import Image


def getNpArrayFromImg(imgPath: str):
    """转化 img 至 np 数组"""
    im = Image.open(imgPath)
    return np.array(im)
