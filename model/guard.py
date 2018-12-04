# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 14:21
#  @description  :  守护
# from flask_sqlalchemy import SQLAlchemy
# import time
# import os

# db = SQLAlchemy()
from . import db

class Table():
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
    TASK_ORDER_NO = db.Column(db.String, primary_key=True, nullable=False)
    ORDER_TYPE = db.Column(db.CHAR)
    TASK_TYPE = db.Column(db.String)
    ACCEPT_PROVINCE_CODE = db.Column(db.String)
    ACCEPT_EPARCHY_CODE = db.Column(db.String)
    ACCEPT_CITY_CODE = db.Column(db.String)
    CREATE_DATE = db.Column(db.DateTime)
    FAIL_NUM = db.Column(db.BIGINT)
    FAIL_RESON = db.Column(db.String)
    REMARK = db.Column(db.String)

    def __repr__(self):
        return 'BatchTask%r[%r]' % (self.REMARK,self.TASK_ORDER_NO)


if __name__ == '__main__':
    engine = db.create_engine('mysql+pymysql://issmadm:issmadm@10.102.255.37:8069/dbissmadm?charset=utf8')
    DBSession = db.sessionmaker(bind=engine)
    dbSession = DBSession()
    dbSession.query(BatchTask).filter_by(TASK_ORDER_NO="10101010").update({'FAIL_NUM':0})
    dbSession.commit()
    batch_task = dbSession.query(BatchTask).filter_by(TASK_ORDER_NO="10101010").one()
    print(batch_task.to_json())
    # time.sleep(10)
    print(dbSession.query(BatchTask.FAIL_NUM).filter_by(TASK_ORDER_NO="10101010").one())
    if(dbSession.query(BatchTask.FAIL_NUM).filter_by(TASK_ORDER_NO="10101010").one()[0]==0):
        print('执行脚本')
        # os.system(u'/iom/script/idaemonshell/idaemon/src/killAssignWoTimer.sh')
        # os.system(u'/iom/script/idaemonshell/idaemon/src/startAssignWoTimer..sh')
        os.system('java -version ')
        os.system('python -V')
