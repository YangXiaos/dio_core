# @Time         : 18-5-26 下午8:13
# @Author       : DioMryang
# @File         : MysqlUtil.py
# @Description  :
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger('dio')


def createConnect(**config):
    """
    创建mysql连接
    :return:
    """
    logger.info("create mysql connect {host}:{port}/{db_name}".format(**config))
    engine = create_engine('mysql+{driver}://{user}:{password}@{host}:{port}/{db_name}?charset=utf8'.format(**config)
                         , encoding='utf-8')
    return sessionmaker(bind=engine)()
