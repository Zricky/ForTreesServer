# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 14:12
#  @description  :
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
from sqlalchemy import Column, String, create_engine, DateTime, BIGINT, CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
