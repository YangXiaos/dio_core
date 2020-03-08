# @Time         : 19-2-7 下午1:49
# @Author       : DioMryang
# @File         : os_util.py
# @Description  :
import os


def find_all_file(dir_path: str):
    """获取所有文件"""
    return os.listdir(dir_path)
