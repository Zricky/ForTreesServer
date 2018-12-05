# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 11:37
#  @description  :  守护主机监控
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
from model.guard import BatchTask, WorkOrderAssign, NoticeSend, TaskDispatch
from . import *
import os
import time


class IssmWatcher:
    def __init__(self, config):
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        DBSession = sessionmaker(bind=engine)
        self.__dbSession = DBSession()

    def batch_task_watcher(self):
        logger.info('模板匹配守护活性检测')
        self.__dbSession.query(BatchTask).filter_by(TASK_ORDER_NO="10101010").update({'FAIL_NUM': 0})
        self.__dbSession.commit()
        time.sleep(10)
        if (self.__dbSession.query(BatchTask.FAIL_NUM).filter_by(TASK_ORDER_NO="10101010").one()[0] == 0):
            logger.info('执行ApplyOrderIssm脚本')
            os.system('sh /iomapp/shell/idaemonshell/idaemon/src/killApplyOrderIssm.sh')
            os.system('sh /iomapp/shell/idaemonshell/idaemon/src/startApplyOrderIssm.sh')
        else:
            logger.info('ApplyOrderIssm keep alive')

    def order_assign_watcher(self):
        logger.info('派单客服守护活性检测')
        self.__dbSession.query(WorkOrderAssign).filter_by(apply_no="10101010").update({'repeat_cnt': 0})
        self.__dbSession.commit()
        time.sleep(10)
        if (self.__dbSession.query(WorkOrderAssign.repeat_cnt).filter_by(apply_no="10101010").one()[0] == 0):
            logger.info('执行AssignWoTimer脚本')
            os.system('sh /iomapp/shell/idaemonshell/idaemon/src/killAssignWoTimer.sh')
            os.system('sh /iomapp/shell/idaemonshell/idaemon/src/startAssignWoTimer.sh')
        else:
            logger.info('AssignWoTimer keep alive')

    def sms_send_watcher(self):
        logger.info('短信派发守护活性检测')
        self.__dbSession.query(NoticeSend).filter_by(NOTICE_ID="10101010").update({'FAIL_NUM': 0})
        self.__dbSession.commit()
        time.sleep(10)
        if (self.__dbSession.query(NoticeSend.FAIL_NUM).filter_by(NOTICE_ID="10101010").one()[0] == 0):
            logger.info('执行NoticeSendTimer脚本')
            os.system('sh /iomapp/shell/idaemonshell/idaemon/src/killNoticeSendTimer.sh')
            os.system('sh /iomapp/shell/idaemonshell/idaemon/src/startNoticeSendTimer.sh')
        else:
            logger.info('NoticeSendTimer keep alive')

    def task_dispatch_watcher(self):
        logger.info('工作流守护活性检测')
        self.__dbSession.query(TaskDispatch).filter_by(msg_id="10101010").update({'msg_deal_count': 0})
        self.__dbSession.commit()
        time.sleep(10)
        if (self.__dbSession.query(TaskDispatch.msg_deal_count).filter_by(msg_id="10101010").one()[0] == 0):
            logger.info('执行taskDispatchshell脚本')
            os.system('sh /iomapp/shell/taskDispatchshell/src/stopnewIdaemon.sh')
            os.system('sh /iomapp/shell/taskDispatchshell/src/startnewIdaemon.sh')
        else:
            logger.info('TaskDispatchshell keep alive')

    def syn_staff_watcher(self):
        logger.info('工号同步守护活性检测')
        name = 'SCStaffCodeSyTimer'
        if (self.__process_is_run(name)):
            logger.info('%s keep alive' % name)
        else:
            logger.info('执行SCStaffCodeSyTimer脚本')
            os.system('sh /iomapp/shell/idaemonshell/idaemon/src/startSCStaffCodeSy.sh')

    def __process_is_run(self, name):
        script = 'ps -ef|grep -v grep|grep java|grep ' + name + '|awk "{print \$2}"'
        if (len(os.popen(script).readlines()) >= 1):
            return True
        else:
            return False
