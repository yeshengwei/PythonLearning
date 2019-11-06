#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

class MusicPlayer(object):
    #重写new方法
    def __new__(cls, *args, **kwargs):
        #创建对象时new方法会被自动调用
        print("创建对象，分配空间...")
        #为对象分配空间
        instance=super().__new__(cls)
        #返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化....")

player=MusicPlayer()

print(player)