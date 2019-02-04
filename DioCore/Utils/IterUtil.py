

def chunks(l, n):
    """
    数据分割
    :param l: 数据列表
    :param n: 分割数
    :return: 分割列表
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]