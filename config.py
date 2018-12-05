# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/4 11:18
#  @description  :  配置文件
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
# 脚本日志 配置项 #
LOGNAME = 'watcher'
# 日志等级 NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL #
# 已经封装 日志等级 对应从 权限低到高 依次为 0  1   2   3   4   5 #
LOG_LEAVEL = 1
LOG_PATH = 'D:\\PycharmProjects\\ForTreesServer\\logs\\'
# 是否写日志到文件开关
IS_WRITE_LOG_TO_FILE = False
IS_REWRITE_FILE = False
class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://issmadm:issmadm@10.102.255.37:8069/dbissmadm?charset=utf8'
    # 当关闭数据库是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 是否追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://issmadm:issmadm@10.102.255.37:8069/dbissmadm?charset=utf8'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://issmadm:issmadm@10.102.255.37:8069/dbissmadm?charset=utf8'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}
