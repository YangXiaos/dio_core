import logging

from DioCore.Network.Downloader import Downloader
from DioCore.Utils import TimeUtil

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

while True:
    soup = Downloader.getBs4("http://proxy.datastory.com.cn/getADAllHost?id=ss-teg")
    logger.info("count:{}".format(soup.select_one("count").text))

    for proxy in soup.select("ips id"):
        logger.info("proxy: {}".format(proxy.text))
    TimeUtil.sleep(10)
