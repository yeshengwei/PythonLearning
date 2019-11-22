#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

try:
    num = int(input("请输入一个整数："))
    result = 8 / num
    print(result)

except ValueError:
    print("请输入正确的整数！")

# 捕获所有未知错误：
except Exception as result:
    print(f"未知错误：{result}")
