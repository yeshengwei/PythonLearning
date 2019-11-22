#!/usr/bin/python
# -*- coding: utf-8 -*-

# 打开文件
file = open("hello.txt", "r")

# 读写文件
text = file.read()
print(text)

print("-" * 50)
# 指针会移动到结尾后，再次读取就无数据了
text = file.read()
print(text)

# 关闭文件
file.close()
