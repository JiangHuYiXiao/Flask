# -*- coding:utf-8 -*-

import flask
from flask import request,jsonify

'''
1、第一个接口，Hello World
@Author:jianghuyixiao,2018-11-19
请求方式：get
返回：Hello:World
地址：http://127.0.0.1:7777/hello_world
'''
sever = flask.Flask(__name__)           # 创建一个服务把当前文件作为一个服务启动
sever.config['JSON_AS-ASCII'] = False   # 不显示Unicode编码格式，显示正常的字符串格式，避免浏览器把中文转换为Unicode而出现乱码
@sever.route('/hello_world',methods = ['get'])
def hello_world():
    return jsonify('Hello'':''World')
sever.run(port = 7777,debug=True)



'''
2、用户查询 select_list
@Author:jianghuyixiao,2018-11-19
请求方式：get
返回：jianghu
地址：http://127.0.0.1:7778/select_list
'''
sever = flask.Flask(__name__)
sever.config['JSON_AS-ASCII'] = False
list = ['jianghu','yixiu','wahaha','qqxing','xiaoaojianghu']
@sever.route('/select_username',methods = ['get'])
def select_list():
    return jsonify(list[0])
sever.run(port = 7778,debug = True)


'''
3、员工信息查询 select_dic
@Author:jianghuyixiao,2018-11-19
请求方式：get
返回:{'name':'jianghu','age':100,'height':180,'sex':'male'}
地址：http://127.0.0.1:7779/select_dic
'''
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



''''
4、增加元素到列表,list = ['jianghu','yixiu','wahaha','qqxing','xiaoaojianghu']
@Author jianghuyixiao 2018-11-20
请求方式：get
返回:list
地址：http://127.0.0.1:7780/list_add?list=hehe
'''
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
