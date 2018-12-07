# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/4 14:59
#  @description  :  脚本入口
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
from script.watcher import IssmWatcher
from config import config
from concurrent.futures import ThreadPoolExecutor
# import threading

env = config['test']
issmWatcher = IssmWatcher(env)
pool = ThreadPoolExecutor()
tasks = [
    issmWatcher.batch_task_watcher,
    issmWatcher.order_assign_watcher,
    issmWatcher.sms_send_watcher,
    issmWatcher.task_dispatch_watcher,
    issmWatcher.syn_staff_watcher
]

def run_tasks():
    for task in tasks:
        # t = threading.Thread(target=task)
        # t.start()
        pool.submit(task)


if __name__ == '__main__':
    run_tasks()
    pool.shutdown(wait=True)
