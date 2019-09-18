import os

import shutil


def delDir(dirPath):
    print("扫描文件目录------- {}".format(dirPath))
    for dir_ in os.listdir(dirPath):
        filePath = os.path.join(dirPath, dir_)
        if os.path.isdir(filePath):
            delDir(filePath)
        else:
            print("删除文件--------- {}".format(filePath))
            os.remove(filePath)
    # print("删除文件--------- {}".format(dirPath))
    # os.remove(dirPath)


if __name__ == '__main__':
    delDir("C:\\Users\\Administrator\\Downloads\\AndroidKiller_v1.3.1\\projects")