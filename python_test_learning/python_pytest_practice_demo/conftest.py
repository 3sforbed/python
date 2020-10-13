#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   conftest.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/12 17:09   banxian      1.0         None
'''
import pytest
import yaml

from python_pytest_practice_demo.pytest_calculator_demo02 import Calculator

''' 编码问题解决方案'''
from typing import List
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
     for item in items:
         item.name = item.name.encode('utf-8').decode('unicode-escape')
         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope="function")
def print_message():
	print("【开始计算】")
	yield
	print("【计算结束】")
@pytest.fixture(scope="module",autouse=True)
def calclass():
	return Calculator

'''
	全局数据初始化
'''
def getdata(filename):
	with open(filename,encoding="UTF-8") as f:
		yaml_data = yaml.safe_load(f)
		return yaml_data

yaml_data_demo2 = getdata("calculator_demo02.yml")
param_data_demo2 = yaml_data_demo2["add"]["data"]
ids_data_demo2 = yaml_data_demo2["add"]["discription"]

'''
	add test data
'''
@pytest.fixture(scope="function",params=param_data_demo2,ids=ids_data_demo2)
def adddata(request):
	return request.param

'''
	fixture use other hooks
'''
@pytest.fixture()
def my_fixture(pytestconfig):
	result = pytestconfig.hook.pytest_my_hook(config = pytestconfig)
	print(result)
	print("use pytest_my_hook")

'''
	registure a new hook
'''
def pytest_addhooks(pluginmanager):
	from python_pytest_practice_demo import my_hooks
	pluginmanager.add_hookspecs(my_hooks)


'''
	注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
'''
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group将下面所有的option都展示在这个group下
    mygroup.addoption("--env",
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )
    mygroup.addoption("--des",
                      default='dev',  # 默认值
                      dest='dev',  # 存储的变量
                      help='set your param'  # 参数说明
                      )
    mygroup.addoption("--dem",
                      default='st',  # 默认值
                      dest='st',  # 存储的变量
                      help='set your param'  # 参数说明
                      )

'''
	env默认值是test,表示测试环境
'''
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')