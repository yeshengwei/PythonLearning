#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: yeshengwei
# E-mail: shw.ye@qq.com

class Game(object):
    # 定义类属性
    top_score = 0

    # 定义类方法
    @classmethod
    def show_top_score(cls):
        print(f"历史最高分为：{cls.top_score}")

    def __init__(self, name):
        # 定义实例属性
        self.name = name

    # 定义静态方法
    @staticmethod
    def show_help():
        print("帮助信息")

    # 定义实例方法
    def start_game(self):
        print(f"{self.name}开始游戏啦...")


# 查看游戏的帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
game = Game("小明")

# 实例调用实例方法
game.start_game()

# 实例方法---方法内部需要访问实例属性
# 类方法---只需要访问类属性
# 静态方法---方法内部，不需要访问实例属性和类属性
#
# 如果方法内部既要访问实例属性，又要访问类属性，应该定义实例方法
