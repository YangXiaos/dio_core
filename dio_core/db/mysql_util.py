# @Time         : 18-5-26 下午8:13
# @Author       : DioMryang
# @File         : mysql_util.py
# @Description  :

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dio_core.utils import logger_util


logger = logger_util.get_logger("mysql_util")


def create_connection(**config):
    """
    创建mysql连接
    :return:
    """
    logger.info("create mysql connect {host}:{port}/{db_name}".format(**config))
    engine = create_engine('mysql+{driver}://{user}:{password}@{host}:{port}/{db_name}?charset=utf8'.format(**config)
                         , encoding='utf-8')
    return sessionmaker(bind=engine)()
