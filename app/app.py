# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/3 11:36
#  @description  :
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python
from flask import Flask, jsonify
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(config['test'])
db.init_app(app)


@app.route('/charts/getStatistics')
def getStatistics():
    from service.service import getStatistics
    response = {
        'data': getStatistics(),
        'status': 200,
        'statusText': 'OK',
        'headers': {},
        'config': {}
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run()
