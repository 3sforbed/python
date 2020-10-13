#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   my_hooks.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/13 20:27   banxian      1.0         None
'''


'''
	a new hook demo
'''
def pytest_my_hook(config) -> object:
	"""
    Receives the pytest config and does things with it
    """
	print("in use pytest_my_hook")
	return config.hook
