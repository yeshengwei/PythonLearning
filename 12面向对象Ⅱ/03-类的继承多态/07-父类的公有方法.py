#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com
# Date  : 2019/11/5
class A():
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test(self):
        print("父类的公有方法")


class B(A):
    def demo(self):
        # 在子类中不能访问父类的私有属性
        print(f"访问父类的私有属性{self.__num2}")

        # 在子类中同样不能访问父类的私有方法
        # self.__test()

        # 访问父类的公有属性
        print(f"父类的公有属性{self.num1}")

        # 调用父类的公有方法
        self.test()


b = B()

# 在外界访问父类的公有属性
print(b.num1)

# 在外界访问父类的公有方法
b.test()
