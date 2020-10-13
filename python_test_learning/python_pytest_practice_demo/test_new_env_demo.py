#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_new_env_demo.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/14 0:16   banxian      1.0         None
'''


def test_demo(cmdoption):
    print(f"env环境下读取的值为:", cmdoption)
    print(f"dev环境下读取的值为:", cmdoption)
    print(f"st环境下读取的值为:", cmdoption)