import random


# 获取随机经纬度定位
import string
from typing import Iterable


def get_random_location():
    x = round(random.randint(100, 130) + random.random(), 6)
    y = round(random.randint(10, 40) + random.random(), 6)
    return y, x


# 获取随机字符串
def get_random_string(num: int) -> str:
    return "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase, num))


# 获取随机元素
def get_random_ele_form_list(l: Iterable):
    return random.choice(l)


if __name__ == '__main__':
    host_list = [
        "2ek6836376.wicp.vip",
        "2ek6836376.wicp.vip:38255"
    ]
    print(get_random_ele_form_list(host_list))