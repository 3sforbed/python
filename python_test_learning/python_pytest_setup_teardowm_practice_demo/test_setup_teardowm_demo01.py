#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_setup_teardowm_demo01.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/12 14:51   banxian      1.0         None
'''

class TestSetupTeardowm(object):
    def setup(self):
        print("setup")
    def teardown(self):
        print("teardown")
    def setup_method(self):
        print("setup_method")
    def teardown_method(self):
        print("teardown_method")
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def test_inclass(self):
        pass

def setup_function():
    print("setup_function")
def teardown_function():
    print("teardown_function")
def setup_module():
    print("setup_module")
def teardown_module():
    print("teardown_module")
def test_outclass():
    pass


'''
    测试结果:
    test_outclass()
        setup_module
        setup_function
        PASSED                      [100%]
        teardown_function
        teardown_module
    test_inclass:
        setup_module
        setup_class
        setup_method
        setup
        PASSED   [100%]
        teardown
        teardown_method
        teardown_class
        teardown_module
'''