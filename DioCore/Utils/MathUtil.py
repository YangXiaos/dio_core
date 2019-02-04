import math
from typing import Tuple


def getDistance(tuple1: Tuple[float, float], tuple2: Tuple[float, float]):
    """获取距离"""
    x1 = tuple1[0]
    x2 = tuple2[0]
    y1 = tuple1[1]
    y2 = tuple2[1]

    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


def geodistance(lat1, lng1, lat2, lng2):
    lng1, lat1, lng2, lat2 = map(math.radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    dis = 2 * math.asin(math.sqrt(a)) * 6371 * 1000
    return dis


if __name__ == '__main__':
    print(geodistance(24.881934, 118.598776, 24.886901, 118.606471))
