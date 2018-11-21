#-*- coding:utf-8 -*-
'''
8、登录 shopping
@Author:jianghuyixiao,2018-11-20
请求方式：post,get
入参：goods_num，your_money
出参：resultcode，reson,msg
地址：http://127.0.0.1:7784/shopping?goods_num=1&your_money=10
'''

import flask
from flask import request,jsonify

sever = flask.Flask(__name__)
sever.config['JSON_AS_ASCII'] = False

@sever.route('/shopping',methods = ['get','post'])
def shopping():
    goods_num = request.values.get('goods_num')
    your_money = request.values.get('your_money')

    # data = request.json
    # goods_num = data[goods_num]
    # your_money = data[your_money]

    list = [{'name': '香蕉', 'price': 10},
            {'name': '苹果', 'price': 4},
            {'name': '橘子', 'price': 5},
            {'name': '哈密瓜', 'price': 20},
            {'name': '火龙果', 'price': 8}]
    shopping_cart = {}

    if int(your_money) <= 4:
        return jsonify({"resultcode":201,
                        "reason": "错误的返回",
                        "msg":"你的资金不够，欢迎下次光临"
                        })

    else:

        if int(goods_num) in range(len(list)):
            if list[int(goods_num)]['name'] not in shopping_cart:
                shopping_cart.setdefault(list[int(goods_num)]['name'],1)

            else:
                shopping_cart.setdefault(shopping_cart[list[int(goods_num)]['name']] + 1)

        remain_money = int(your_money) -  list[int(goods_num)]['price']   #shopping_cart[list[int(goods_num)]['name']]*
        if remain_money < 0:
            return jsonify({"resultcode": 202,
                            "reason": "错误的返回",
                            "msg": "你所剩的余额不多，请充值"
                            })
        print(shopping_cart)
        return jsonify({"resultcode":200,
                        "reason": "正确的返回",
                        "msg":shopping_cart
                        })
# shopping()
sever.run(port = 7784,debug = True)