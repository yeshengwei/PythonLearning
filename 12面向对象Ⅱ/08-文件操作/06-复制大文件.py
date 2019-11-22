#!/usr/bin/python
# -*- coding: utf-8 -*-

# 打开文件
file_read = open("hello.txt")
file_write = open("hello_write.txt", "w")

# 读写操作
while True:
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break
    # 写入新文件
    file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()
