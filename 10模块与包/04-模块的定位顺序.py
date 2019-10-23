# 自己的文件名不能和已有模块重名，如果重复无法使用
# import random
# num=random.randint(1,100)
# print(num)

def sleep():
    print("我是自定义的sleep")

from time import sleep
# def sleep():
#     print("我是自定义的sleep")

sleep(3)
