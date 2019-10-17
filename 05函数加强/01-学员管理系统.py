# 显示功能界面
def infoPrint():
    print("\n\n---------请选择功能---------")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员")
    print("4.查询学员")
    print("5.显示全部")
    print("6.退出系统")
    print("*" * 26)


info = []


# 添加学员的函数
def addInfo():
    """添加学员的函数"""
    # 用户输入学号姓名手机号
    newId = input("请输入您的学号：")
    newName = input("请输入您的姓名：")
    newTel = input("请输入您的电话：")

    # 判断是否有重名
    for i in info:
        if newName == i["name"]:
            print("此学员已存在，无须添加！")
            return

    # 添加学员信息
    infoDict = {}
    infoDict["id"] = newId
    infoDict["name"] = newName
    infoDict["tel"] = newTel

    # 列表追加字典
    info.append(infoDict)


# 删除学员的函数
def delInfo():
    delName = input("请输入您要删除的学员姓名：")
    global info
    for i in info:
        if delName == i["name"]:
            info.remove(i)
            break
    else:
        print("您输入的学员不存在！")


# 修改学员的函数
def modifyInfo():
    modifyName = input("请输入您要修改的学员姓名：")
    global info
    for i in info:
        if modifyName == i["name"]:
            i["tel"] = input("请输入新的手机号：")
            print("学员信息修改成功！")
            break
    else:
        print("您输入的学员不存在！")


# 查询学员的函数
def searchInfo():
    searchName = input("请输入您要查询的学员姓名：")
    global info
    for i in info:
        if searchName == i["name"]:
            print("查询结果如下：")
            print(f"您查询的学员的学号是:{i['id']},姓名是:{i['name']},电话号码是:{i['tel']}")
            break
    else:
        print("您输入的学员不存在！")


# 打印所有学员函数

def printAll():
    """显示所有学员信息"""
    print("学号\t姓名\t电话\t")
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


# 重复执行
while True:
    infoPrint()

    # 用户选择功能
    userNum = int(input("请选择您需要的功能："))

    # 根据用户输入的序号执行不同的函数
    if userNum == 1:
        addInfo()
    elif userNum == 2:
        delInfo()
    elif userNum == 3:
        modifyInfo()
    elif userNum == 4:
        searchInfo()
    elif userNum == 5:
        printAll()
    elif userNum == 6:
        exitFlag = input("您确定要退出系统吗？请输入 yes or no ：")
        if exitFlag == "yes":
            break
    else:
        print("输入错误，请重新输入！")
