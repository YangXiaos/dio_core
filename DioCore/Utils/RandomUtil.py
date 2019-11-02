import random
import string
from typing import Iterable, TypeVar


T = TypeVar('T')


# 列表随机获取元素
def getRandomEleFromList(l: Iterable[T]) -> T:
    return random.choice(l)


# 获取随机字符串
def getRandomString(num: int) -> T:
    return "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase, num))


if __name__ == '__main__':
    print(getRandomString(5))
