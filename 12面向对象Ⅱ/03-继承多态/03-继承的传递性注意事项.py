#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com
# Date  : 2019/11/4
class Animal():
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


# 继承父类Animal的方法，子类拥有父类的所有属性和方法
class Dog(Animal):

    def bark(self):
        print("叫---")

#继承父类Dog的方法
class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")

#继承父类Animal的方法
class Cat(Animal):
    def catch(self):
        print("抓老鼠...")


wangcai = XiaoTianQuan()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

