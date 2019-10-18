# @Time         : 18-6-28 下午9:08
# @Author       : DioMryang
# @File         : ThreadUtil.py
# @Description  :
import threading

import threadpool


def getCurrentThreadName():
    """
    获取当前线程名
    :return:
    """
    return threading.current_thread().ident


def multiThreadingRun(fuc, argsList=None, threadNum=5, commonArgs=None, commonKwargs=None):
    """
    多线程处理函数
    :param commonKwargs:
    :param commonArgs: 共同参数
    :param threadNum:
    :param fuc:
    :param argsList:
    :return:
    """
    if commonArgs is not None:
        argsList = [(commonArgs, None)] * threadNum
    elif commonKwargs is not None:
        argsList = [(commonKwargs, None)] * threadNum
    elif argsList is None:
        argsList = range(threadNum)

    pool = threadpool.ThreadPool(threadNum)
    requests = threadpool.makeRequests(fuc, argsList)
    [pool.putRequest(req) for req in requests]
    pool.wait()


def multiThreadingRunWithCommonArgs(fuc, argsList=None, threadNum=5):
    pass


def multiThreadRun(fuc, threadNum=3):
    """
    多线程跑数无参跑数
    :param fuc:
    :param threadNum:
    :return:
    """
    pool = threadpool.ThreadPool(threadNum)
    requests = threadpool.makeRequests(fuc, args_list=range(threadNum))
    [pool.putRequest(req) for req in requests]
    pool.wait()



if __name__ == '__main__':
    print(getCurrentThreadName())
