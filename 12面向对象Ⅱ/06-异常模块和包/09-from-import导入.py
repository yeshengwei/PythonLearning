#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

from module1 import Dog
from module2 import say_hello

#直接使用工具名使用，不需要再使用  模块名.工具名 的方式
say_hello()

mydog=Dog()
print(mydog)