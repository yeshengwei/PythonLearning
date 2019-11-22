#!/usr/bin/python
# -*- coding: utf-8 -*-

# 打开文件
file = open("ExportData.csv", "r")

# 读写文件
text = file.read()
print(text)

# 关闭文件
file.close()
