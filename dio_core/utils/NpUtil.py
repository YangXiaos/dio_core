# @Time         : 19-2-7 下午4:48
# @Author       : DioMryang
# @File         : NpUtil.py
# @Description  :
import numpy as np
from PIL import Image


def get_np_array_from_img(img_path: str):
    """转化 img 至 np 数组"""
    im = Image.open(img_path)
    return np.array(im)
