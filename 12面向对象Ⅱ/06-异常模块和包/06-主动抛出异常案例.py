#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

def input_password():
    # 提示用户输入密码
    pwd = input("请输入密码：")
    # 判断密码长度，如果密码长度大于等于8，返回用户密码
    if len(pwd) >= 8:
        return pwd

    # 如果密码小于8主动抛出异常
    # 创建异常对象
    ex = Exception("密码长度不够！")
    # 主动抛出异常
    raise ex

try:
    print(input_password())

except Exception as result:
    print(result)
