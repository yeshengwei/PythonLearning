# 批量重命名文件名
import os

# os.chdir("test")
# fileList=os.listdir()
# # print(fileList)
# for i in fileList:
#     newName="python-"+i
#     os.rename(i,newName)

# 删除批量的重命名
os.chdir("test")
flag = 1
fileList = os.listdir()
for i in fileList:
    if flag == 1:
        newName = "python-" + i
    elif flag == 2:
        num = len("python-")
        newName = i[num:]
    os.rename(i, newName)
