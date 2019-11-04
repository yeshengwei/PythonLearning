#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com
# Date  : 2019/11/4

class Women():
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def secret(self):
        print(f"{self.name}的年龄是{self.__age}岁。")


xiaofang = Women("小芳")

# 私有属性不能被外界访问
# print(xiaofang.__age)


xiaofang.secret()
