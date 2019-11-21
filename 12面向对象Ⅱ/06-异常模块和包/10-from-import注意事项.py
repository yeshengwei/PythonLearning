#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

# from module1 import say_hello
from module2 import say_hello
from module1 import say_hello as M1_say_hello

#从2个模块中导入同名的方法
say_hello()
M1_say_hello()


#后导入的会覆盖先导入的