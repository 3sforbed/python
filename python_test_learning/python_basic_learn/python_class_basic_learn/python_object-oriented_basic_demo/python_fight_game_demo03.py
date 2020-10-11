#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   python_fight_game_demo03.py    
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/11 18:13   banxian      1.0         None
'''

# 快捷键导入 alt + enter（回车）
# 文件名、 路径名、 变量名、函数名、类名，不要和python内置库冲突
from python_test_learning.python_basic_learn.python_manitulate_3rd_part_data_source_learn.python_manipulate_yaml_data_demo.python_manipulate_yml_data_demo03 import \
    Game


class HouYi(Game):
    # 子类的init 构造方法覆盖掉了父类的构造方法
    def __init__(self, houyi_hp, your_hp, defense):
        # 继承父类的构造方法,
        # 使用关键字传参方式，给game 父类传参
        super().__init__(my_hp=houyi_hp, your_hp=your_hp)
        self.defense = defense

    def fight(self):
        # 对打多轮，谁的血量先小于等于0，谁就输了
        while True:
            self.my_hp = self.my_hp + self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            if self.my_hp<=0:
                # pycharm 快捷键， ctrl+D 可以复制当前行
                print("后裔的剩余血量为",self.my_hp)
                print("你的剩余血量为",self.your_hp)
                print("后裔输了")
                break
            elif self.your_hp <= 0:
                print("后裔的剩余血量为",self.my_hp)
                print("你的剩余血量为",self.your_hp)
                print("你输了")
                break


houyi = HouYi(1000, 1000 ,100)
houyi.fight()
