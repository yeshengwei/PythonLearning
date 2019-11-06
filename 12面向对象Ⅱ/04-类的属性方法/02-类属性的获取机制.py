#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

class Tool(object):
    # 定义类的属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 通过对象名从下向上查找获取类属性，建议使用类名获取
print(tool1.count)

print(tool2.count)
