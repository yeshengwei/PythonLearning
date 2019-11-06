#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com
# Date  : 2019/11/5

class A():
    def test(self):
        print("testA")

    def demo(self):
        print("demoA")


class B():
    def demo(self):
        print("demoB")

    def test(self):
        print("testB")


# 继承A/B,AB类中有同名的方法
class C(A, B):
    pass


# 创建子类对象
xiaoc = C()

# 如果继承多个父类有同名的方法和属性，避免使用多继承
xiaoc.test()
xiaoc.demo()

# 确定C类对象调用父类方法的顺序
print(C.__mro__)
