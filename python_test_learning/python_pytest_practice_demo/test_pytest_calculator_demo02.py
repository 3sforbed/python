#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_pytest_calculator_demo02.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/12 16:04   banxian      1.0         None
'''

import pytest

'''
    1、补全计算器（加减乘除）的测试用例
    2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
    3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
    4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
    5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别
'''


class TestCalculator(object):
    '''
        fixture(param = []) 方式传参
    '''
    @pytest.mark.usefixtures("print_message")
    def test_add(self,calclass,adddata,my_fixture):
        assert calclass.add(adddata[0],adddata[1]) == adddata[2]

    @pytest.mark.usefixtures("print_message")
    def test_minus(self,calclass):
        pass

    @pytest.mark.usefixtures("print_message")
    def test_multi(self,calclass):
        pass

    @pytest.mark.usefixtures("print_message")
    def test_divide(self,calclass):
        pass
