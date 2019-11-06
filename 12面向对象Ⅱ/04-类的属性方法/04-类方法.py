#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print(f"工具对象的数量{cls.count}")

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# 创建对象
tool1 = Tool("斧头")

tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()
