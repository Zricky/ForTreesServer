# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 14:21
#  @description  :  守护
# from flask_sqlalchemy import SQLAlchemy
# import time
# import os

# = SQLAlchemy()
from . import *


class Table():
    def to_json(self):
        from datetime import datetime
        dict = self.__dict__
        dict.pop('_sa_instance_state')
        for item in dict:
            if (isinstance(dict[item], datetime)):
                dict[item] = str(dict[item])
        return dict


class BatchTask(Base, Table):
    __tablename__ = 'tf_b_batch_task'
    TASK_ORDER_NO = Column(String, primary_key=True, nullable=False)
    ORDER_TYPE = Column(CHAR)
    TASK_TYPE = Column(String)
    ACCEPT_PROVINCE_CODE = Column(String)
    ACCEPT_EPARCHY_CODE = Column(String)
    ACCEPT_CITY_CODE = Column(String)
    CREATE_DATE = Column(DateTime)
    FAIL_NUM = Column(BIGINT)
    FAIL_RESON = Column(String)
    REMARK = Column(String)

    def __repr__(self):
        return 'BatchTask%r[%r]' % (self.REMARK, self.TASK_ORDER_NO)


class WorkOrderAssign(Base, Table):
    __tablename__ = 'tf_b_work_order_assign'
    APPLY_NO = Column(String, primary_key=True, nullable=False)
    WORK_ORDER_NO = Column(String)
    ACCEPT_PROVINCE_CODE = Column(String)
    ACCEPT_EPARCHY_CODE = Column(String)
    ACCEPT_EPARCHY_CODE = Column(String)
    ACCEPT_CITY_CODE = Column(String)
    WORK_MODE = Column(CHAR(1))
    STEP_ID = Column(String)
    STATE = Column(CHAR(3))
    STATE_DATE = Column(DateTime)
    CREATE_DATE = Column(DateTime)
    DEAL_SYS = Column(CHAR(3))
    DEAL_MSG = Column(String)
    REPEAT_CNT = Column(BIGINT(10))
    REMARK = Column(String)
    PRI = Column(CHAR(3))

    def __repr__(self):
        return 'WorkOrderAssign%r[%r]' % (self.REMARK, self.APPLY_NO)


class NoticeSend(Base, Table):
    __tablename__ = 'tf_b_notice'
    NOTICE_ID = Column(String, primary_key=True, nullable=False)
    ACCEPT_PROVINCE_CODE = Column(String)
    ACCEPT_EPARCHY_CODE = Column(String)
    OP_NO = Column(String)
    OP_TYPE = Column(CHAR(1))
    PRI = Column(CHAR(3))
    NOTICE_TYPE = Column(CHAR(3))
    NOTICE_TOPIC = Column(String)
    NOTICE_DESC = Column(String)
    ASSIGN_STAFF_ID = Column(String)
    ASSIGN_STAFF_NAME = Column(String)
    ASSIGN_DEPART_ID = Column(String)
    ASSIGN_DEPART_NAME = Column(String)
    RECEIVE_STAFF_ID = Column(String)
    RECEIVE_STAFF_NAME = Column(String)
    RECEIVE_DEPART_ID = Column(String)
    RECEIVE_DEPART_NAME = Column(String)
    STATE = Column(CHAR)
    STATE_DATE = Column(DateTime)
    CREATE_DATE = Column(DateTime)
    FAIL_NUM = Column(BIGINT(5))
    FAIL_REASON = Column(String)
    REMARK = Column(String)
    TEMPLATE_ID = Column(String)
    CONTACT_NUM = Column(String)
    SEND_DATE = Column(DateTime)
    APPLY_NO = Column(String)
    WORK_ORDER_NO = Column(String)

    def __repr__(self):
        return 'NoticeSend%r[%r]' % (self.REMARK, self.NOTICE_ID)

class TaskDispatch(Base, Table):
    __tablename__ = 'or_task_dispatch'
    NOTICE_ID = Column(String, primary_key=True, nullable=False)
    ACCEPT_PROVINCE_CODE = Column(String)
    ACCEPT_EPARCHY_CODE = Column(String)
    OP_NO = Column(String)
    OP_TYPE = Column(CHAR(1))
    PRI = Column(CHAR(3))
    NOTICE_TYPE = Column(CHAR(3))
    NOTICE_TOPIC = Column(String)
    NOTICE_DESC = Column(String)
    ASSIGN_STAFF_ID = Column(String)
    ASSIGN_STAFF_NAME = Column(String)
    ASSIGN_DEPART_ID = Column(String)
    ASSIGN_DEPART_NAME = Column(String)
    RECEIVE_STAFF_ID = Column(String)
    RECEIVE_STAFF_NAME = Column(String)
    RECEIVE_DEPART_ID = Column(String)
    RECEIVE_DEPART_NAME = Column(String)
    STATE = Column(CHAR)
    STATE_DATE = Column(DateTime)
    CREATE_DATE = Column(DateTime)
    FAIL_NUM = Column(BIGINT(5))
    FAIL_REASON = Column(String)
    REMARK = Column(String)
    TEMPLATE_ID = Column(String)
    CONTACT_NUM = Column(String)
    SEND_DATE = Column(DateTime)
    APPLY_NO = Column(String)
    WORK_ORDER_NO = Column(String)

    def __repr__(self):
        return 'WorkOrderAssign%r[%r]' % (self.REMARK, self.APPLY_NO)
