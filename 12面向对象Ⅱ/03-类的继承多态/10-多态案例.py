#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f"{self.name}蹦蹦跳跳的玩耍...")


class XiaoTianQuan(Dog):
    def game(self):
        print(f"{self.name}飞到天上去玩耍...")


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print(f"{self.name}和{dog.name}愉快的玩耍...")
        dog.game()


# # 创建一个狗对象
# wangcai=Dog("旺财")

# 创建一个狗对象
wangcai = XiaoTianQuan("旺财")

# 创建一个人对象
xiaomin = Person("小明")

# 让人调用和狗玩的方法
xiaomin.game_with_dog(wangcai)
