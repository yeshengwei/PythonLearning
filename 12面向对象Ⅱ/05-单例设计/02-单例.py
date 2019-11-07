#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

class MusicPlayer(object):
    # 定义一个类属性，记录第一个被创建对象的引用
    instance = None

    # 对new方法进行改造
    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类的方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
