# # 文件指针在开头
# file=open("test.txt","r+")
# print(file.read())
# file.close()

# # 没有文件会新建，文件指针在开头，内容被覆盖
# file=open("test.txt","w+")
# print(file.read())
# file.close()

# 没有文件会新建，文件指针在结尾，无法读取数据，指针后面没有数据
# file=open("test.txt","r+")
file = open("test.txt", "a+")
# file.seek(0,0)
file.seek(0)
text = file.read()
print(text)

file.close()
