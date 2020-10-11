#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_fight_game_demo01.py
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/10 22:01   banxian      1.0         None
'''

'''
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''

def lol():#定义游戏方法
    #声明4个变量，分别为两个角色的生命值和攻击力
    theshy_hp=1000
    theshy_ad=300
    new_hp=1000
    new_ad=200

    while True:#当循环结构，条件为真时执行循环
        theshy_hp = theshy_hp - new_ad
        new_hp = new_hp - theshy_hp
        #生命值计算方法


        if theshy_hp <= 0:# 判定游戏胜负条件
            print('gg,new win')
            break
            #break退出循环
        elif new_hp <= 0:
            print('gg,theshy win')
            break

lol()#调用游戏方法
