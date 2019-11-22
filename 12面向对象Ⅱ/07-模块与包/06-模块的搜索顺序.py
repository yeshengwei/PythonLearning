#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com


# 如果有random文件时程序会出错，因为和系统函数重名
import random

# 查看模块物理路径
print(random.__file__)

rand = random.randint(0, 9)

print(rand)
