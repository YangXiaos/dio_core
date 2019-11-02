from DioCore.Utils import TextUtil


def main(time: str, requestNum: int, tp: str="", ):
    h = TextUtil.getFirstMatch(time, "(\d+)h,")
    m = TextUtil.getFirstMatch(time, "(\d+)m")
    s = TextUtil.getFirstMatch(time, "(\d+)s")

    h = int(h) if h is not None else 0
    m = int(m) if m is not None else 0
    s = int(s) if s is not None else 0
    time = h * 60 * 60 + m * 60 + s
    print("{} 耗时{}s".format(tp, time), "速度{} s/次".format(time//requestNum))


def main2(time: str, time2: str, requestNum: int, requestNum2: int, tp: str="", ):
    h = TextUtil.getFirstMatch(time, "(\d+)h,")
    m = TextUtil.getFirstMatch(time, "(\d+)m")
    s = TextUtil.getFirstMatch(time, "(\d+)s")

    h = int(h) if h is not None else 0
    m = int(m) if m is not None else 0
    s = int(s) if s is not None else 0
    time = h * 60 * 60 + m * 60 + s

    h2 = TextUtil.getFirstMatch(time2, "(\d+)h,")
    m2 = TextUtil.getFirstMatch(time2, "(\d+)m")
    s2 = TextUtil.getFirstMatch(time2, "(\d+)s")

    h2 = int(h2) if h2 is not None else 0
    m2 = int(m2) if m2 is not None else 0
    s2 = int(s2) if s2 is not None else 0
    time2 = h2 * 60 * 60 + m2 * 60 + s2

    print("{} 耗时{}s".format(tp, time2 - time), "速度{} s/次".format((time2 - time)//(requestNum2 - requestNum)))


if __name__ == '__main__':
    # main("24h,9m,3s", 595, "商品")
    # main("191h,19m,43s", 116 + int(48762/10), "评论")
    # main("189h,2m,17s", 35126 + 5026, "子评论")
    #
    # main("5h,55m,26s", 1078, "商品")
    # main("61h,37m,29s", 11 + 256 + 136454/10, "评论")
    # main("3h,6m,39s", 340, "商品")
    # main2("3h,57m,7s", "6h,25m,38s", 389, 450)
    # main("114h,28m,58s", 3183, "cmt")
    main("471h,25m,4s", 191392, "cmt")

