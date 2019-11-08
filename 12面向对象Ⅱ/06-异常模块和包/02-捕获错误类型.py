#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)

# 针对不同错误类型，进行不同的处理方式：
except ZeroDivisionError:
    print("除数不能为0！")

# 针对不同错误类型，进行不同的处理方式：
except ValueError:
    print("请确认输入值为整数！")

