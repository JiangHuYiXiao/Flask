#-*- coding:utf-8 -*-
''''
4、增加元素到列表,list = ['jianghu','yixiu','wahaha','qqxing','xiaoaojianghu']
@Author jianghuyixiao 2018-11-20
请求方式：get
返回:list
地址：http://127.0.0.1:7780/list_add?list=hehe
'''
import flask
from flask import request,jsonify
sever = flask.Flask(__name__)
sever.config['JSON_AS_ASCII'] = False

@sever.route('/list_add',methods = ['get'])
def list_add():
    list = ['jianghu', 'yixiu', 'wahaha', 'qqxing', 'xiaoaojianghu']
    L = request.values.get('list')
    # data = request.json
    # L = data[list]
    list.append(L)
    res = list
    return jsonify(res)

sever.run(port = 7780,debug = True)