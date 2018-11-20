#-*- coding:utf-8 -*-
'''
import flask

from flask import request

from flask import jsonify

import tools

import OP_db

import settings



flask： web框架，可以通过flask提供的装饰器@server.route()将普通函数转换为服务

登录接口，需要传url、username、passwd



 #创建一个服务，把当前这个python文件当做一个服务

server = flask.Flask(__name__)

server.config['JSON_AS_ASCII'] = False



# @server.route()可以将普通函数转变为服务  登录接口的路径、请求方式

@server.route('/login', methods=['get'])

def login():

    username = request.values.get('name')

    pwd = request.values.get('pwd')

     # 判断用户名、密码都不为空，如果不传用户名、密码则username和pwd为None

    if username and pwd:

        # 获取加密后的密码

        password = tools.md5_pwd(pwd)

        #执行sql，如果查询的username和password不为空，说明数据库存在admin的账号

        sql = 'select name,password from test where name= "%s" and password= "%s";' %(username, password)

         # 从数据查询结果后，res返回是元组

        res = OP_db.getconn(

            host=settings.mysql_info['host'],

            user=settings.mysql_info['user'],

            passwd=settings.mysql_info['pwd'],

            db=settings.mysql_info['db'],

            port=settings.mysql_info['port'],

            sql=sql

        )

        if res:      #res的结果不为空，说明找到了username=admin的用户，且password为加密前的123456

            resu = {'code': 200, 'message': '登录成功'}

            return jsonify(resu) #将字典转换为json串, json是字符串

         else:

             resu = {'code': -1, 'message': '账号/密码错误'}

            return jsonify(resu)

    else:

       res = {'code': 999, 'message': '必填参数未填写'}

       return jsonify(res)



if __name__ == '__main__':

      server.run(debug=True, port=8899, host=0.0.0.0)  #指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
'''
# import json
# from urllib.parse import parse_qs
# from wsgiref.simple_server import make_server
#
# def application(environ,start_repsonse):
#     start_repsonse('200,ok',[('Content-Type','text/html')])
#     params = parse_qs(environ(['QUERY_STRING']))
#     name = params.get('name',[''])[0]
#     no = params.get('no',[''])[0]
#     dic = {'name':name,'no':no}
#     return [json.dumps(dic)]
#
# if __name__ == '__main__':
#     port = 5688
#     httpd = make_server('127.0.0.1',port,application)
#     print('serving http on port {0}...'.format(str(port)))
#     httpd.serve_forever()


# import json
# from urllib.parse import parse_qs
# from wsgiref.simple_server import make_server
#
#
# # 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
# def application(environ, start_response):
#     # 定义文件请求的类型和当前请求成功的code
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
#     # 获取当前get请求的所有数据，返回是string类型
#     params = parse_qs(environ['QUERY_STRING'])
#     # 获取get中key为name的值
#     name = params.get('name',[''])[0]
#     no = params.get('no',[''])[0]
#
#     # 组成一个数组，数组中只有一个字典
#     dic = {'name': name, 'no': no}
#
#     return [json.dumps(dic)]
#
#
# if __name__ == "__main__":
#     port = 5088
#     httpd = make_server("0.0.0.0", port, application)
#     print("serving http on port {0}...".format(str(port)))
#     httpd.serve_forever()






import flask
from flask import request,jsonify

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