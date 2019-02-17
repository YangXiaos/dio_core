from DioCore.Utils import ImageUtil, OsUtil


def test_resize():
    dir_ = "/home/mryang/Project/dio_algo/datasets/cat/"
    for imgPath in OsUtil.findAllFile(dir_):
        imgPath = dir_ + imgPath
        ImageUtil.resize(imgPath, (100, 100), imgPath.replace("/cat/", "/cat_target/"))


def test_resize_1():
    ImageUtil.resize("/home/mryang/Project/dio_algo/datasets/cat_test/dio.jpg",
                     (100, 100), "/home/mryang/Project/dio_algo/datasets/cat_test/dio_target.jpg")