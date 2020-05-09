#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   login.py
@Time    :   2020/5/9 14:49
@Author  :   jiangheng
@Desc    :   
"""

import flask

# 获取参数
from flask import request, jsonify
import json

# 创建 flask 对象
app = flask.Flask(__name__)

def connect_sql(sql):
    pass

@app.route('/login', methods=['POST', 'GET'])
def login():
    phone_number = request.values.get('phone_number')
    phone_code = request.values.get('phone_code')

    if phone_number and phone_code:
        if phone_code == 200:
            return jsonify(
                {
                    "phone_number": phone_number,
                    "phone": phone_code
                }
            )
        else:
            return jsonify("error")
    else:
        return jsonify("please input phone number and code")


if __name__ == "__main__":
    app.run(port=8000, debug=True)