import logging

from dio_core.network.downloader import Downloader
from dio_core.utils import time_util

logger = logging.get_logger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

while True:
    soup = Downloader.get_bs4("http://proxy.datastory.com.cn/getADAllHost?id=ss-teg")
    logger.info("count:{}".format(soup.select_one("count").text))

    for proxy in soup.select("ips id"):
        logger.info("proxy: {}".format(proxy.text))
    time_util.sleep(10)
