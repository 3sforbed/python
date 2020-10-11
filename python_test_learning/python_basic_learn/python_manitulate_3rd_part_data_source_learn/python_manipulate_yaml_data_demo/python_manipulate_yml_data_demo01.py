#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_manipulate_yml_data_demo01.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/11 11:36   banxian      1.0         None
'''

import yaml

yaml_data = yaml.safe_load(open("data.yml",encoding="utf-8"))
print(yaml_data)
print(type(yaml_data))
a = [[{'a':1},'admin2'],'admin3']
with open("data3","w") as f:
    yaml.safe_dump(a,f)