#-*- coding:utf-8 -*-
'''
5、获取文件：致橡树
@Author jianghuyixiao 2018-11-20
请求方式：get
返回:文件
地址：http://127.0.0.1:7781/search_file
'''
import flask
from flask import request,jsonify
import os
sever = flask.Flask(__name__)
sever.config['JSON_AS_ASCII'] = False

@sever.route('/search_file',methods = ['get'])
def search_file():
    list = []
    with open('致橡树',mode = 'r+',encoding = 'utf-8') as file:
        for i in file:
            list.append(i.strip())
        res = list
        return jsonify(res)

sever.run(port = 7781,debug = True)