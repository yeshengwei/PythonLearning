#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

class Dog(object):

    # 不需要访问类的属性和方法，也不需要访问对象的属性和方法，因此使用静态方法，不需要传递第一个参数
    @staticmethod
    def run():
        print("小狗跑...")


# 调用静态方法，在没有任何对象的时候可以调用
Dog.run()
