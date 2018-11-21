#-*- coding:utf-8 -*-
'''
3、员工信息查询 select_dic
@Author:jianghuyixiao,2018-11-19
请求方式：get
返回:{'name':'jianghu','age':100,'height':180,'sex':'male'}
地址：http://127.0.0.1:7779/select_dic
'''
import flask
from flask import request,jsonify
sever = flask.Flask(__name__)
sever.config['JSON_AS_ASCII'] = False
dict = [
    {'name':'jianghu','age':100,'height':180,'sex':'male'},
    {'name':'yixiu','age':8,'height':180,'sex':'male'},
    {'name':'wahaha','age':25,'height':30,'sex':'male'},
    {'name':'qqxing','age':18,'height':170,'sex':'female'},
    {'name':'zixiaxianzi','age':17,'height':170,'sex':'female'},
        ]
@sever.route('/select_dic',methods = ['get'])
def select_dic():
    return jsonify(dict[0])
sever.run(port = 7779,debug = True)