# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 11:36
#  @description  :
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
