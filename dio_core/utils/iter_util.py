

def chunks(eles, n):
    """
    数据分割
    :param eles: 数据列表
    :param n: 分割数
    :return: 分割列表
    """
    for i in range(0, len(eles), n):
        yield eles[i:i + n]
