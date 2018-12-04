# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/4 14:59
#  @description  :  脚本入口
from script.watcher import batch_task_watcher
from config import config

env = config['test']

if __name__ == '__main__':
    batch_task_watcher(env)
