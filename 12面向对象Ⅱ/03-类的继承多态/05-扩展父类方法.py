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
        print("汪汪叫---")


# 继承父类Dog的方法
class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        # 针对子类特有的需求编写代码
        print("叫的跟神一样...")
        # 使用super()调用父类的方法1
        super().bark()
        # 使用父类名称调用父类的方法2
        # Dog.bark(self)
        # 增加其它子类的代码
        print("其它叫法")


xtq = XiaoTianQuan()
xtq.bark()
