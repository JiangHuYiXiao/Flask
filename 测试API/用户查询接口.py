#-*- coding:utf-8 -*-
'''
2、用户查询 select_list
@Author:jianghuyixiao,2018-11-19
请求方式：get
返回：jianghu
地址：http://127.0.0.1:7778/select_list
'''
import flask
from flask import request,jsonify
sever = flask.Flask(__name__)
sever.config['JSON_AS-ASCII'] = False
list = ['jianghu','yixiu','wahaha','qqxing','xiaoaojianghu']
@sever.route('/select_username',methods = ['get'])
def select_list():
    return jsonify(list[0])
sever.run(port = 7778,debug = True)