#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_pytest_calculator_demo01.py
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/11 21:52   banxian      1.0         None
'''
import pytest
import math
import yaml

from python_pytest_practice_demo.pytest_calculator_demo01 import Calculator

'''
    Prerequest: calculator_demo01.yml data source
                pytest
                pyyaml
                pytest-ordering
                
    Calculator: plus minus multiply divide
    
    Detail:
        1、补全计算器（加法 除法）的测试用例
        2、使用参数化完成测试用例的自动生成
        3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
    注意:
        使用等价类，边界值，因果图等设计测试用例
        测试用例中添加断言，验证结果
        灵活使用 setup(), teardown() , setup_class(), teardown_class()
        
'''
class TestCalculator(object):
    @classmethod
    def setup_class(self):
        print("【初始化测试类资源】")
    @classmethod
    def teardown_class(self):
        print("【测试完成，回收测试类资源】")
    def setup(self):
        print("【开始计算】")
    def teardown(self):
        print("【计算结束】")

    ''' 
        @pytest.mark.addtest    自定义mark，通过命令行 pytest -m addtest 指定特定测试用例执行
        @pytest.mark.run(order = 1)     指定测试用例的执行顺序，0为最高优先级
        @pytest.mark.parametrize("a,b",[[1,1],[1,2]])   参数化用例的第一种方式，直接在parameterize中指定用例数据，适用于小数据量
    '''
    @pytest.mark.addtest
    @pytest.mark.run(order = 0)
    @pytest.mark.parametrize("a,b",[[1,1],[1,2]],ids = ["11","22"])
    def test_add(self,a,b):
        try:
            assert math.fsum([a,b]) == Calculator.add(a,b)
            print()
        except  TypeError as e:
            print(e)
        finally:
            pass

    ''' 
        @pytest.mark.minustest
        @pytest.mark.run(order=1)
        @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("calculator_demo01.yml"))["minus"])   参数化用例的第二种方式
    '''
    @pytest.mark.minustest
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("calculator_demo01.yml"))["minus"])
    def test_minus(self,a,b,expect):
        try:
            assert Calculator.minus(a,b) == expect
            print()
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e + "【the expect result of the expr is : " + expect + "】")
        finally:
            pass

    ''' 
        @pytest.mark.multest
        @pytest.mark.run(order=2)
        @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("calculator_demo01.yml"))["multi"])
    '''
    @pytest.mark.multest
    @pytest.mark.run(order = 2)
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("calculator_demo01.yml"))["multi"])
    def test_multi(self,a,b,expect):
        try:
            assert Calculator.multi(a,b) == expect
            print()
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e + "【the expect result of the expr is : " + expect + "】")
        finally:
            pass

    '''
        @pytest.mark.divtest
        @pytest.mark.run(order = default)   默认次序在所有正数的后面，在所有负数的前面
        @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("calculator_demo01.yml"))["divide"])
    '''
    @pytest.mark.divtest
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("calculator_demo01.yml"))["divide"])
    def test_divide(self,a,b,expect):
        try:
            assert Calculator.divide(a,b) == expect
            print()
        except TypeError as e:
            print(e)
        except Exception as e:
            print("\n" + str(e) + " occur.【while the expect result is : " + expect + "】")
        finally:
            pass

