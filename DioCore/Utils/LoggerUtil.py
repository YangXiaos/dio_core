import logging


logging.basicConfig(level=logging.INFO, filemode='w',
                    format="[%(asctime)s]-[%(name)s]-[%(levelname)s]-[%(thread)d:%(threadName)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S",)


def getLogger(cls):
    if isinstance(cls, str):
        logger = logging.getLogger(cls)
    else:
        logger = logging.getLogger(cls.__name__)
    return logger
