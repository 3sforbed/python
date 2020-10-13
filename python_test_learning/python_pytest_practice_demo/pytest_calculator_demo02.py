#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pytest_calculator_demo02.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/12 17:05   banxian      1.0         None
'''

'''
    输入数据：整形，浮点型
    输出数据：整型，浮点型
    注意：
        对输入类型和输出类型判断
        对数据精度处理 ，如：1/3 == 0.3333333333333333
        溢出情况处理      
'''

class Calculator(object):
    @classmethod
    def add(self,a,b):
        if isinstance(a,int) and isinstance(b,int):
            return a + b
        else:
            raise TypeError("请输入正确的数字，type(a):" + type(a) + ".type(b):" + type(b) + ".")
    @classmethod
    def minus(self,a,b):
        if isinstance(a,int) and isinstance(b,int):
            return a - b
        else:
            raise TypeError("请输入正确的数字，type(a):" + type(a) + ".type(b):" + type(b) + ".")
    @classmethod
    def multi(self,a,b):
        if isinstance(a,int) and isinstance(b,int):
            return a * b
        else:
            raise TypeError("请输入正确的数字，type(a):" + type(a) + ".type(b):" + type(b) + ".")
    @classmethod
    def divide(self,a,b):
        if isinstance(a,int) and isinstance(b,int):
            if b == 0:
                raise Exception("divided by zero error")
            else:
                return a / b
        else:
            raise TypeError("请输入正确的数字，type(a):" + type(a) + ".type(b):" + type(b) + ".")