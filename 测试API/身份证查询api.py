# -*- coding:utf-8 -*-
'''
6、身份证校验 id_card
@Author:jianghuyixiao,2018-11-20
请求方式：post
入参：cardno
出参：errcode，msg,reson
地址：http://127.0.0.1:7783/id_card?card_no=110101199003075656
'''
import flask
from flask import request,jsonify
sever = flask.Flask(__name__)
sever.config['JSON_AS_ASCII'] = False

@sever.route('/id_card',methods = ['get','post'])
def id_card():
    u = request.values.get('card_no')
    # data = request.json
    # u = data[card_no]
    if len(u) == 18:
        for i in u[:-2:]:
            isdigit = i.isdigit()
            if isdigit:
                sum = int(u[0]) * 7 + int(u[1]) * 9 + int(u[2]) * 10 + int(u[3]) * 5 +int(u[4]) * 8 + int(u[5]) * 4 + int(u[6]) * 2 + int(u[7]) * 1\
                      + int(u[8]) * 6 + int(u[9]) * 3 + int(u[10]) * 7 + int(u[11]) * 9 + int(u[12]) * 10 + int(u[13]) * 5 + int(u[14]) * 8 + int(u[15]) * 4 + int(u[16]) * 2
                print(sum,type(sum))
                if sum % 11 == 0:
                    cal_last_str = 1
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 1:
                    cal_last_str = 0
                    if int(u[-1]) != cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 2:
                    cal_last_str = 'X'
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 3:
                    cal_last_str = 9
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 4:
                    cal_last_str = 8
                    if int(u[-1]) != cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 5:
                    cal_last_str = 7
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 6:
                    cal_last_str = 6
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 7:
                    cal_last_str = 5
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 8:
                    cal_last_str = 4
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })
                if sum % 11 == 9:
                    cal_last_str = 3
                    if int(u[-1]) == cal_last_str:
                        print({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        print({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })


                if sum % 11 == 10:
                    cal_last_str = 2
                    if int(u[-1]) == cal_last_str:
                        return jsonify({"resultcode": 200,
                                        "reason": "正确的的返回",
                                        "msg": "身份证号码有效"
                                        })
                    else:
                        return jsonify({"resultcode": 203,
                                        "reason": "错误的返回",
                                        "msg": "身份证号码无效"
                                        })

            else:
                return jsonify({"resultcode":201,
                                "reason": "错误的返回",
                                "msg":"身份证号码前17位只能是数字"
                                })
    else:
        return jsonify({"resultcode": 202,
                        "reason": "错误的返回",
                        "msg": "身份证号码的长度必须是18"
                        })
sever.run(port = 7783,debug = True)
