#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File  : 03-案例实践-士兵突击.py
# Author: yeshengwei
# Date  : 2019/11/1
# 创建枪类
class Gun():
    def __init__(self, model):
        # 初始化枪的型号
        self.model = model
        # 初始化子弹数量
        self.bullet_count = 0

    # 定义添加子弹方法
    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print(f"{self.model}没有子弹了！")
            return

        # 发射子弹
        self.bullet_count -= 1

        # 提示发射信息
        print(f"突突突...")


# 创建枪对象ak47
ak47 = Gun("AK47")


# 创建士兵类
class Soldier():
    def __init__(self, name):
        # 定义新兵的姓名
        self.name = name

        # 定义一个枪的属性,不确定枪的类型，所以设置为None
        self.gun = None

    # 定义士兵开枪的方法
    def fire(self):
        # 判断士兵是否有枪
        if self.gun == None:
            print(f"该士兵没有枪!")
            return

        # 士兵高喊口号
        print(f"[{self.name}]冲啊...")

        # 装填子弹
        self.gun.add_bullet(100)

        # 发射子弹
        self.gun.shoot()


# 创建许三多
xusanduo = Soldier("许三多")

# 将枪交给许三多
xusanduo.gun = ak47

# 许三多开枪
xusanduo.fire()

print(xusanduo.gun)
