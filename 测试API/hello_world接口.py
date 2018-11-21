#-*- coding:utf-8 -*-
'''
1、第一个接口，Hello World
@Author:jianghuyixiao,2018-11-19
请求方式：get
返回：Hello:World
地址：http://127.0.0.1:7777/hello_world
'''
import flask
from flask import request,jsonify
sever = flask.Flask(__name__)           # 创建一个服务把当前文件作为一个服务启动
sever.config['JSON_AS-ASCII'] = False   # 不显示Unicode编码格式，显示正常的字符串格式，避免浏览器把中文转换为Unicode而出现乱码
@sever.route('/hello_world',methods = ['get'])
def hello_world():
    return jsonify('Hello'':''World')
sever.run(port = 7777,debug=True)


