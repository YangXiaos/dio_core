# @Time         : 18-6-7 上午8:37
# @Author       : DioMryang
# @File         : ModuleUnit.py
# @Description  : 模块加载类
import importlib
import logging


def loadModule(modulePath=""):
    """
    动态加载模块
    :param modulePath: 模块路径
    :return:
    """
    return importlib.import_module(modulePath)


def loadClass(absClassPath=""):
    """
    加载类
    :param absClassPath: 类
    :return:
    """
    logging.info("加载 {}".format(absClassPath))
    _ = absClassPath.split(".")
    modulePath, className = ".".join(_[0:-1]), _[-1]
    m = loadModule(modulePath)
    return getattr(m, className)


if __name__ == '__main__':
    loadModule("DioFramework.Processor.JobProcessor.JobSeedReader")
