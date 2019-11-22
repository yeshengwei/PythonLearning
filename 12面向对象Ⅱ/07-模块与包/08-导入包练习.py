#!/usr/bin/python
# -*- coding: utf-8 -*-

# 导入包package
import package

package.send_message.send("hello")
text = package.receive_message.receive()
print(text)
