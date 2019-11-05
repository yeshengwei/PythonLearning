#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com
# Date  : 2019/11/5
class A():
    def __init__(self):
        self.num1=100
        self.__num2=200

    def __test(self):
        print(f"私有方法{self.num1},{self.__num2}")

class B(A):
    def demo(self):
        #在子类中不能访问父类的私有属性
        print(f"访问父类的私有属性{self.__num2}")

        #在子类中同样不能访问父类的私有方法
        # self.__test()
        pass

b=B()
print(b.num1)

#在外界不能访问对象的私有属性
# print(b.__num2)

#在外界不能访问对象的私有方法
# b.__test()


