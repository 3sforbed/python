#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_manipulate_xlsx_data_demo03.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/11 11:30   banxian      1.0         None
'''
from openpyxl import load_workbook

'''
    Read an existing workbook
'''

wb = load_workbook(filename = 'empty_book.xlsx')
sheet_ranges = wb['range names']
print(sheet_ranges['D18'].value)
