#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com
def demo1():
    return int(input("请输入一个整数："))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    demo2()
except Exception as result:
    print(f"未知错误:{result}")
