#!/usr/bin/python
# -*- coding: utf-8 -*-

file = open("hello.txt")

while True:
    text = file.readline()
    if not text:
        break
    print(text)

file.close()
