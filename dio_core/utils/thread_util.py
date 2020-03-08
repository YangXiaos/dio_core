# @Time         : 18-6-28 下午9:08
# @Author       : DioMryang
# @File         : thread_util.py
# @Description  :
import threading

import threadpool


def get_current_thread_name():
    """
    获取当前线程名
    :return:
    """
    return threading.current_thread().ident


def multi_threading_run(fuc, args_list=None, thread_num=5, common_args=None, common_kwargs=None):
    """
    多线程处理函数
    :param common_kwargs:
    :param common_args: 共同参数
    :param thread_num:
    :param fuc:
    :param args_list:
    :return:
    """
    if common_args is not None:
        args_list = [(common_args, None)] * thread_num
    elif common_kwargs is not None:
        args_list = [(common_kwargs, None)] * thread_num
    elif args_list is None:
        args_list = range(thread_num)

    pool = threadpool.ThreadPool(thread_num)
    requests = threadpool.makeRequests(fuc, args_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()


def multi_threading_run_with_common_args(fuc, args_list=None, thread_num=5):
    pass


def multi_thread_run(fuc, thread_num=3):
    """
    多线程跑数无参跑数
    :param fuc:
    :param thread_num:
    :return:
    """
    pool = threadpool.ThreadPool(thread_num)
    requests = threadpool.makeRequests(fuc, args_list=range(thread_num))
    [pool.putRequest(req) for req in requests]
    pool.wait()



if __name__ == '__main__':
    print(get_current_thread_name())
