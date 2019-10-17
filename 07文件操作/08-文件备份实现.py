# 用户输入目标文件
oldName = input("请输入您要备份的文件名称：")
# 规划备份文件的名称
index = oldName.rfind(".")
name = oldName[:index]

if index > 0:

    # print(name)

    newName = name + "-backup" + oldName[index:]
    print(newName)

    # 写入数据

    oldFile = open(oldName, "rb")
    newFile = open(newName, "wb")

    while True:
        con = oldFile.read(1024)
        newFile.write(con)
        if len(con) == 0:
            break
    oldFile.close()
    newFile.close()

else:
    print("输入错误，请重新输入！")
