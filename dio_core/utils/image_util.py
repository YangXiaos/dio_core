# @Time         : 19-2-7 下午1:56
# @Author       : DioMryang
# @File         : image_util.py
# @Description  :
import cv2
from PIL import Image
from typing import Tuple
from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity


def resize(img_path: str, size: Tuple, target: str = ""):
    """图片 resize"""
    img = Image.open(img_path)
    tmp = img.resize(size, Image.ANTIALIAS)
    img.close()
    tmp.save(target if target else img_path)


def crop(img_path: str, to_path: str, left: int, top: int, right: int, bottom: int):
    """ 图片 截取"""
    img = Image.open(img_path)
    img = img.crop((left, top, right, bottom))
    img.save(img_path if to_path is None else img_path)


def compare_img(img_path1: str, img_path2: str):
    """图片 比较"""
    image_a = cv2.imread(img_path1)
    image_b = cv2.imread(img_path2)

    gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
    gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

    score = structural_similarity(gray_a, gray_b)
    return score


if __name__ == '__main__':
    compare_img(r"C:\Users\Administrator\Desktop\dio_core\DioCore\Tools\AdbTool\temp.1.png", r"C:\Users\Administrator\Desktop\dio_core\DioCore\Tools\AdbTool\temp.png")
