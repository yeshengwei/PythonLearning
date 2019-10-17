

# 没有文件会新建，文件指针在结尾，无法读取数据，指针后面没有数据
file=open("test.txt","a+")
print(file.seek(2,0))
file.close()