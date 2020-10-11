#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_manipulate_yml_data_demo02.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/11 17:48   banxian      1.0         None
'''

import yaml

data = yaml.safe_load(open("game.yml"))
# 打印出来yaml转换的字典
print(data)
# 打印出来yaml转换的字典中，key值为me对应的value
print(data["me"])
# 打印出来yaml转换的字典中，key值为me对应的value 的 key值对应为"hp"

print(data["me"]["hp"])
