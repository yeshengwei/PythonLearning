#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1.建立setup.py文件

# 引入构建包信息的模块
from distutils.core import setup

# 定义发布的包文件的信息
setup(
    name="package",  # 发布的包的名称
    version="1.00.001",  # 发布包的版本序号
    description="test",  # 发布包的描述信息
    author="leaf",  # 发布包的作者信息
    author_email="shw.ye@qq.com",  # 作者的联系邮箱
    url="www.baidu.com",  # 作者主页
    py_modules=["send_message", "receive_message"]  # 发布包中的模块文件列表
)

# #2.构建模块
# python setup.py build

# #3.生成发布压缩包
# python setup.py sdist

# -----------------------------------------------------------------------------------------
# #安装模块
# tar -zxvf xxxx.tar.gz
# cd xxxx
# python setup.py install

# ------------------------------------------------------------------------------------------

# #卸载模块
# 直接删除包文件的目录即可 rm -rf 模块

# 安装第三方模块
# pip install pygame
