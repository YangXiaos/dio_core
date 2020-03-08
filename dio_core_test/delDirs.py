import os

import shutil


def delDir(dir_path):
    print("扫描文件目录------- {}".format(dir_path))
    for dir_ in os.listdir(dir_path):
        file_path = os.path.join(dir_path, dir_)
        if os.path.isdir(file_path):
            delDir(file_path)
        else:
            print("删除文件--------- {}".format(file_path))
            os.remove(file_path)
    # print("删除文件--------- {}".format(dir_path))
    # os.remove(dir_path)


if __name__ == '__main__':
    delDir("C:\\Users\\Administrator\\Downloads\\AndroidKiller_v1.3.1\\projects")