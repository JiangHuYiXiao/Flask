# -*- coding:utf-8 -*-

import flask
from flask import request,jsonify
#
# '''
# 1、第一个接口，Hello World
# @Author:jianghuyixiao,2018-11-19
# 请求方式：get
# 返回：Hello:World
# '''
# sever = flask.Flask(__name__)
# sever.config['JSON_AS-ASCII'] = False
# @sever.route('/hello_world',methods = ['get'])
# def hello_world():
#     return jsonify('Hello'':''World')
# sever.run(port = 6677,debug=True)
#
#
#
# '''
# 1、用户查询 select_list
# @Author:jianghuyixiao,2018-11-19
# 请求方式：get
# 返回：jianghu
# '''
# sever = flask.Flask(__name__)           # 创建一个服务把当前文件作为一个服务启动
# sever.config['JSON_AS-ASCII'] = False   # 不显示Unicode编码格式，显示正常的字符串格式，避免浏览器把中文转换为Unicode而出现乱码
# list = ['jianghu','yixiu','wahaha','qqxing','xiaoaojianghu']
# @sever.route('/select_username',methods = ['get'])
# def select_list():
#     return jsonify(list[0])
# sever.run(port = 7786,debug = True)
#
#
# '''
# 2、员工信息查询 select_dic
# @Author:jianghuyixiao,2018-11-19
# 请求方式：get
# 返回:{'name':'jianghu','age':100,'height':180,'sex':'male'}
# '''
# sever = flask.Flask(__name__)           # 创建一个服务把当前文件作为一个服务启动
# sever.config['JSON_AS_ASCII'] = False   # 不显示Unicode编码格式，显示正常的字符串格式，避免浏览器把中文转换为Unicode而出现乱码
# dict = [
#     {'name':'jianghu','age':100,'height':180,'sex':'male'},
#     {'name':'yixiu','age':8,'height':180,'sex':'male'},
#     {'name':'wahaha','age':25,'height':30,'sex':'male'},
#     {'name':'qqxing','age':18,'height':170,'sex':'female'},
#     {'name':'zixiaxianzi','age':17,'height':170,'sex':'female'},
#         ]
# @sever.route('/select_dic',methods = ['get'])
# def select_dic():
#     return jsonify(dict[0])
# sever.run(port = 7787,debug = True)
#
#
# '''


















'''
6、登录 login 
@Author:jianghuyixiao,2018-11-19
请求方式：post
入参：username，pass_word
出参：errcode，msg
'''
sever = flask.Flask(__name__)
sever.config['JSON_AS_ASCII'] = False
username = 'admin'
pass_word = '123'

@sever.route('/login',methods = ['get'])
def login():
    u = request.values.get('username')
    p = request.values.get('pass_word')
    # data = request.json
    # u = data[username]
    # p = data[pass_word]

    if u and p:
        if u == username and p == pass_word:
            res = {'errcode':0,'msg':'ok'}
        else:
            res = {'errcode':1000,'msg':'账号或者密码错误'}
    else:
        res = {'errcode':1001,'msg':'必填参数未填写'}
    return jsonify(res)

sever.run(port = 7788,debug = True)


# https://www.cnblogs.com/alan-babyblog/p/5940493.html
# http://www.php.cn/python-tutorials-373157.html
# https://cloud.tencent.com/developer/article/1087184
