# @Time         : 19-2-7 下午1:49
# @Author       : DioMryang
# @File         : OsUtil.py
# @Description  :
import os


def findAllFile(dirPath: str):
    """获取所有文件"""
    return os.listdir(dirPath)
