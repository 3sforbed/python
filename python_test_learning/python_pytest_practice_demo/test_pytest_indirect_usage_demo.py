#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_pytest_indirect_usage_demo.py
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/12 23:57   banxian      1.0         None
'''
import pytest


@pytest.fixture()
def sayhello(request):
    return "hello " + request.param
@pytest.mark.parametrize("sayhello",["1","2","3"],indirect=True)
def test_say(sayhello):
    print(sayhello)