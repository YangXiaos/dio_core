# @Time         : 19-2-7 下午1:56
# @Author       : DioMryang
# @File         : ImageUtil.py
# @Description  :
import cv2
from PIL import Image
from typing import Tuple
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity


def resize(imgPath: str, size: Tuple, target: str = ""):
    """图片 resize"""
    img = Image.open(imgPath)
    tmp = img.resize(size, Image.ANTIALIAS)
    img.close()
    tmp.save(target if target else imgPath)


def crop(imgPath: str, toPath: str, left: int, top: int, right: int, bottom: int):
    """ 图片 截取"""
    img = Image.open(imgPath)
    img = img.crop((left, top, right, bottom))
    img.save(imgPath if toPath is None else imgPath)


def compareImg(imgPath1: str, imgPath2: str):
    """图片 比较"""
    imageA = cv2.imread(imgPath1)
    imageB = cv2.imread(imgPath2)

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    score = structural_similarity(grayA, grayB)
    return score


if __name__ == '__main__':
    compareImg(r"C:\Users\Administrator\Desktop\dio_core\DioCore\Tools\AdbTool\temp.1.png", r"C:\Users\Administrator\Desktop\dio_core\DioCore\Tools\AdbTool\temp.png")
