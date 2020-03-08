# @Time         : 18-6-7 上午8:37
# @Author       : DioMryang
# @File         : module_util.py
# @Description  : 模块加载类
import importlib
import logging


def load_module(module_path=""):
    """
    动态加载模块
    :param module_path: 模块路径
    :return:
    """
    return importlib.import_module(module_path)


def load_class(abs_class_path=""):
    """
    加载类
    :param abs_class_path: 类
    :return:
    """
    logging.info("加载 {}".format(abs_class_path))
    _ = abs_class_path.split(".")
    module_path, class_name = ".".join(_[0:-1]), _[-1]
    m = load_module(module_path)
    return getattr(m, class_name)


if __name__ == '__main__':
    load_module("DioFramework.Processor.JobProcessor.JobSeedReader")
