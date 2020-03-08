from dio_core.utils import image_util, os_util


def test_resize():
    dir_ = "/home/mryang/Project/dio_algo/datasets/cat/"
    for img_path in os_util.find_all_file(dir_):
        img_path = dir_ + img_path
        image_util.resize(img_path, (100, 100), img_path.replace("/cat/", "/cat_target/"))


def test_resize_1():
    image_util.resize("/home/mryang/Project/dio_algo/datasets/cat_test/dio.jpg",
                      (100, 100), "/home/mryang/Project/dio_algo/datasets/cat_test/dio_target.jpg")