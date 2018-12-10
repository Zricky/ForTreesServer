# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 14:21
#  @description  :  守护
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
# from flask_sqlalchemy import SQLAlchemy
# import time
# import os

# db = SQLAlchemy()
from . import *


class Table:
    def to_json(self):
        from datetime import datetime
        dict = self.__dict__
        dict.pop('_sa_instance_state')
        for item in dict:
            if(isinstance(dict[item],datetime)):
                dict[item]=str(dict[item])
        return dict


class BatchTask(db.Model, Table):
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


class WorkOrderAssign(db.Model, Table):
    __tablename__ = 'tf_b_work_order_assign'
    apply_no = Column(String, primary_key=True, nullable=True)
    work_order_no = Column(String, primary_key=False, nullable=False)
    accept_province_code = Column(String, primary_key=False, nullable=False)
    accept_eparchy_code = Column(String, primary_key=False, nullable=False)
    accept_city_code = Column(String, primary_key=False, nullable=True)
    work_mode = Column(CHAR(1), primary_key=False, nullable=False)
    step_id = Column(String, primary_key=False, nullable=False)
    state = Column(CHAR(3), primary_key=False, nullable=False)
    state_date = Column(DateTime, primary_key=False, nullable=False)
    create_date = Column(DateTime, primary_key=False, nullable=False)
    deal_sys = Column(CHAR(3), primary_key=False, nullable=False)
    deal_msg = Column(String, primary_key=False, nullable=True)
    repeat_cnt = Column(BIGINT, primary_key=False, nullable=True)
    remark = Column(String, primary_key=False, nullable=True)
    pri = Column(CHAR(3), primary_key=False, nullable=True)


class NoticeSend(db.Model, Table):
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
    FAIL_NUM = Column(BIGINT)
    FAIL_REASON = Column(String)
    REMARK = Column(String)
    TEMPLATE_ID = Column(String)
    CONTACT_NUM = Column(String)
    SEND_DATE = Column(DateTime)
    APPLY_NO = Column(String)
    WORK_ORDER_NO = Column(String)

    def __repr__(self):
        return 'NoticeSend%r[%r]' % (self.REMARK, self.NOTICE_ID)


class TaskDispatch(db.Model, Table):
    __tablename__ = 'or_task_dispatch'
    msg_id = Column(String, primary_key=True, nullable=False)
    msg_create_date = Column(DateTime, primary_key=False, nullable=True)
    msg_deal_date = Column(DateTime, primary_key=False, nullable=True)
    msg_deal_flag = Column(CHAR(1), primary_key=False, nullable=True)
    msg_deal_count = Column(BIGINT, primary_key=False, nullable=True)
    msg_fail_reason = Column(String, primary_key=False, nullable=True)
    so_nbr = Column(String, primary_key=False, nullable=True)
    remarks = Column(String, primary_key=False, nullable=True)
    province_code = Column(String, primary_key=False, nullable=True)
    partition_id = Column(BIGINT, primary_key=False, nullable=True)
    task_type = Column(String, primary_key=False, nullable=True)
    wf_id = Column(String, primary_key=False, nullable=True)

    def __repr__(self):
        return 'TaskDispatch%r[%r]' % (self.remarks, self.msg_id)
