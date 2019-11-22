#!/usr/bin/python
# -*- coding: utf-8 -*-

# 打开文件
file_read = open("hello.txt")
file_write = open("hello_write.txt", "w")

# 读写操作
# 读出原文件的所有内容
text = file_read.read()

# 写入到新的文件中
file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()
