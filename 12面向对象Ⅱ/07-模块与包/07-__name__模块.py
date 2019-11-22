#!/usr/bin/python
# -*- coding: utf-8 -*-

# 全局变量，函数，类 直接执行的代码不是向外界提供的工具

def say_helo():
    print("hello")


# 直接执行的代码不需要被执行
print("小明编写的模块")

# 解决方法,在将要导入的模块中添加以下__name__判断，这样其它被调用时不会执行 测试等代码
if __name__ == "__main__":
    print(__name__)
