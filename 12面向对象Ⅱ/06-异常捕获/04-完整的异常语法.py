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


except Exception as result:
    print(f"未知错误：{result}")

else:
    print("尝试执行的代码正确执行时执行")

finally:
    print("无论是否出现错误都会被执行的代码")

print("-" * 50)
