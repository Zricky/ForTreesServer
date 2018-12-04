# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 11:37
#  @description  :  守护主机监控
from smodel.guard import BatchTask
from . import *
import os


def batch_task_watcher(config):
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    DBSession = sessionmaker(bind=engine)
    dbSession = DBSession()
    dbSession.query(BatchTask).filter_by(TASK_ORDER_NO="10101010").update({'FAIL_NUM': 0})
    dbSession.commit()
    # batch_task = dbSession.query(BatchTask).filter_by(TASK_ORDER_NO="10101010").one()
    # print(batch_task.to_json())
    # time.sleep(10)
    # print(dbSession.query(BatchTask.FAIL_NUM).filter_by(TASK_ORDER_NO="10101010").one())
    if (dbSession.query(BatchTask.FAIL_NUM).filter_by(TASK_ORDER_NO="10101010").one()[0] == 0):
        logger.info('执行脚本')
        # os.system('sh /iomapp/script/idaemonshell/idaemon/src/killApplyOrderIssm.sh')
        # os.system('sh /iomapp/script/idaemonshell/idaemon/src/startApplyOrderIssm.sh')
        os.system('java -version ')
        os.system('python -V')
    else:
        logger.info('ApplyOrderIssm keep alive')

