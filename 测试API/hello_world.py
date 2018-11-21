#-*- coding:utf-8 -*-
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

# from flask import Flask
# import flask
# from flask_restful import reqparse, abort, Api, Resource
#
# app =Flask(__name__)
# api = Api(app)
#
# Tasks = {
#     't1': {'task': 'eat an app'},
#     't2': {'task': 'play football'},
#     't3': {'task': 'watching TV'},
# }
#
# def abort_if_todo_doesnt_exist(t_id):
#     if t_id not in Tasks:
#         abort(404, message="Todo {} doesn't exist".format(t_id))
#
#
# parser = reqparse.RequestParser()
# parser.add_argument('task', type=str)
#
#
# # 获取  &  更新
# class Get_Modify(Resource):
#     # def get(self):
#     #     return Tasks
#     def post(self):
#         args = parser.parse_args()
#         t_id = int(max(Tasks.keys()).lstrip('t')) + 1
#         t_id = 't%i' % t_id
#         Tasks[t_id] = {'task': args['task']}
#         return Tasks[t_id], 201
#
#
# # # 设置每个视图函数的访问格式
# api.add_resource(Get_Modify, '/get_modify')
#
# if __name__ == '__main__':
#     app.run(debug=True)


import flask
from flask import request,jsonify
''''
# 增加元素到列表,list:list = ['jianghu','yixiu','wahaha','qqxing','xiaoaojianghu']
# @Author jianghuyixiao 2018-11-19
# 请求方式：get
# 返回:list
# 地址：http://127.0.0.1:7799/list_add?list=hehe
# '''
#
# sever = flask.Flask(__name__)
# sever.config['JSON_AS_ASCII'] = False
#
# @sever.route('/list_add',methods = ['get'])
# def list_add():
#     list = ['jianghu', 'yixiu', 'wahaha', 'qqxing', 'xiaoaojianghu']
#     L = request.values.get('list')
#     # data = request.json
#     # L = data[list]
#     list.append(L)
#     res = list
#     return jsonify(res)
#
# sever.run(port = 7799,debug = True)

'''
获取文件：致橡树
@Author jianghuyixiao 2018-11-20
请求方式：get
返回:文件
地址：http://127.0.0.1:7798/search_file
'''
# import flask
# from flask import request,jsonify
# import os
# sever = flask.Flask(__name__)
# sever.config['JSON_AS_ASCII'] = False
#
# @sever.route('/search_file',methods = ['get'])
# def search_file():
#     list = []
#     with open('致橡树',mode = 'r+',encoding = 'utf-8') as file:
#         for i in file:
#             list.append(i.strip())
#         res = list
#         return jsonify(res)
#
# sever.run(port = 7798,debug = True)

# coding:utf-8
import requests
url = "http://japi.juhe.cn/qqevaluate/qq"
par = {
      "key": "******************",  # appkey需要注册申请
      "qq":  "283340479"
       }
r = requests.get(url, params=par)
print(r.text)  # 打印文本
res = r.json()  # 返回的是json,用r.json解析器转成字典
# 字典取某个字段
conclusion = res["result"]["data"]["conclusion"]
print(conclusion)
analysis = res["result"]["data"]["analysis"]
print(analysis)

