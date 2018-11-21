# -*- coding:utf-8 -*-

import flask
from flask import request,jsonify

'''
6、登录 login 
@Author:jianghuyixiao,2018-11-19
请求方式：post
入参：username，pass_word
出参：errcode，msg
地址：http://127.0.0.1:7782/login?username=ooo,pass_word=1
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

sever.run(port = 7782,debug = True)

# https://www.cnblogs.com/alan-babyblog/p/5940493.html
# http://www.php.cn/python-tutorials-373157.html
# https://cloud.tencent.com/developer/article/1087184
