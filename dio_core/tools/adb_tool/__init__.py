# Author: YangXiaoShuai
# Date: 2019/10/22 16:31
# Project / File: dio_core : __init__.py 
# Desc:
import os

from dio_core.utils import image_util


class Adb(object):
    """
    adb ctroll unit
    """
    def __init__(self, deviceId: str):
        self.deviceId = deviceId

    def getWindowSize(self):
        return self.execute("shell \"dumpsys window displays | grep init= \" ")

    def execute(self, script):
        """execute adb script"""
        result = os.popen("adb -s {} {}".format(self.deviceId, script))
        lines = map(lambda line: line.strip(), result.read().split("\n"))
        return list(lines)

    def getScreenShot(self, img_path: str = None):
        """ get phone screen shot"""
        self.execute("shell screencap -p /sdcard/temp.png")
        self.execute("pull /sdcard/temp.png {}".format(img_path))

    def tap(self, x, y):
        self.execute("shell input tap {} {}".format(x, y))

    def turnback(self):
        self.execute("shell input keyevent 4")

if __name__ == '__main__':
    # Adb("2ad0c47e0205").getScreenShot("temp.png")
    # Adb("2ad0c47e0205").tap(930, 1070)
    Adb("2ad0c47e0205").turnback()

    # ImageUtil.crop("temp.png", None, 0, 530, 1080, 1185)
