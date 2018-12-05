# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/8/15 9:59
#  @description  :  日志封装类
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
import logging
from . import *
log_level_dict = {
    0: logging.NOTSET,
    1: logging.DEBUG,
    2: logging.INFO,
    3: logging.WARNING,
    4: logging.ERROR,
    5: logging.CRITICAL
}


class Logger(object):
    def __init__(self) :
        self.logger = logging.getLogger(LOGNAME)
        self.logger.setLevel(level=log_level_dict[LOG_LEAVEL])
        console = logging.StreamHandler()
        console.setLevel(log_level_dict[LOG_LEAVEL])
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console.setFormatter(formatter)
        self.logger.addHandler(console)
        if (IS_WRITE_LOG_TO_FILE):
            mode='a'
            if(IS_REWRITE_FILE):
                mode='w'
            log_name = '{path}{name}-log.log'.format(path=LOG_PATH, name=LOGNAME)
            handler = logging.FileHandler(log_name, encoding='utf-8',mode=mode)
            handler.setLevel(log_level_dict[LOG_LEAVEL])
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    logger = Logger().get_logger()
    logger.debug(u'走发件方静安路附近阿里')
    logger.info('走发件方静安路附近阿里')
    logger.warning('走发件方静安路附近阿里')
    logger.error('走发件方静安路附近阿里')
    logger.critical('走发件方静安路附近阿里')
