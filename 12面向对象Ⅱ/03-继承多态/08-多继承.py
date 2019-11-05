#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com
# Date  : 2019/11/5

class A():
    def test(self):
        print("test")


class B():
    def demo(self):
        print("demo")

#继承A/B
class C(A,B):
    pass

#创建子类对象
xiaoc=C()
#调用父类A中封装的方法
xiaoc.test()

#调用父类B中封装的方法
xiaoc.demo()

