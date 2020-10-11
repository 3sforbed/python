#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   object_oriented_basic_demo01.py
@Contact :   wangdamar@gmail.com
@License :   GPL v3

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/11 8:12   banxian      1.0         None
'''

'''
 object oriented demo
 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为3个
 
 '''
class Car():
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return "<< my car brand is:" + self.brand + ",The price is:" + self.price.__str__() + ">>"

class Home():
    def __init__(self,location,price):
        self.location = location
        self.price = price

    def __str__(self):
        return "<< my home location is:" + self.location + ",The price is:" + self.price.__str__() + ">>"

class People():
    def __init__(self, name: object, age: object, car: object = None, home: object = None) -> object:
        """

        :param name: people name
        :param age: people age
        :param car: does the people have car
        :param home: does the people have home
        """
        self.name = name
        self.age = age
        self.car = car
        self.home = home

    def __str__(self) -> object:
        """
        :return : return the string of people
        """
        return "my name is:" + self.name + ". my age is:" + self.age.__str__() + ". my car detail is:" \
               + self.car.__str__() + ". my home detail is:" + self.home.__str__() + "."

    def show(self):
        print("hello, my name is",self.name)


if __name__ == '__main__':
    car = Car("tuolaji",5000)
    home = Home("xi'an",200000)
    print(People("jason",23,car,home))