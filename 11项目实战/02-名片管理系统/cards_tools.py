# ！/usr/bin/python
# 存储所有的名片字典
cardList = []


def showMenu():
    """显示菜单"""
    print("\n欢迎使用[名片管理系统]v1.0")
    print("******************************\n"
          "1.新增名片\n"
          "2.显示全部\n"
          "3.查询名片\n"
          "0.退出系统\n"
          "******************************")


def addCard():
    """新增名片"""
    # 提示用户输入名片详细信息
    name = input("请输入姓名：")
    tel = input("请输入电话：")
    qq = input("请输入QQ：")
    mail = input("请输入邮箱：")

    # 根据用户的信息建议字典
    cardDict = {
        "name": name,
        "tel": tel,
        "qq": qq,
        "mail": mail
    }

    # 将名片字典添加到列表
    cardList.append(cardDict)
    print("添加 %s 的名片成功！" % name)


def showCard():
    """显示所有名片"""
    # 判断是否存在名片记录，如果无记录，则直接返回
    if len(cardList) < 1:
        print("当前系统无任何名片，请首先添加名片！")
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")

    # 打印分割线
    print(30 * "-")

    # 遍历字典中value的值
    for i in cardList:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (i["name"], i["tel"], i["qq"], i["mail"]))


def searchCard():
    """查询名片"""
    # 提示用户输入要查询的姓名
    findName = input("请输入您要查询的姓名：")

    # 遍历所有名片列表，如果没有提示用户
    for i in cardList:
        if i["name"] == findName:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print(30 * "-")
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (i["name"], i["tel"], i["qq"], i["mail"]))

            # 针对找到的名片记录进行修改或删除的动作
            # 调用名片处理函数
            dealCard(i)
            break
    # 未找到名片，提示用户
    else:
        print(f"抱歉，{findName}在系统中未找到，请重新输入！")


def dealCard(findDict):
    action = input("请选择您要进行的操作："
                   "[1]修改 "
                   "[2]删除 "
                   "[0]返回: ")

    # 修改字典中的信息
    if action == "1":
        findDict["name"] = inpuCard(findDict["name"], "请输入新的姓名[直接回车不修改]：")
        findDict["tel"] = inpuCard(findDict["tel"], "请输入新的电话[直接回车不修改]：")
        findDict["qq"] = inpuCard(findDict["qq"], "请输入新的QQ[直接回车不修改]：")
        findDict["mail"] = inpuCard(findDict["mail"], "请输入新的邮箱[直接回车不修改]：")
        print("名片修改成功！")

    # 从列表中删除字典
    elif action == "2":
        cardList.remove(findDict)
        print("名片删除成功！")


def inpuCard(dictValue, inputText):
    """提示用户输入内容，如果用户输入内容，直接返回结果，如果用户没有输入内容返回字典字典中原有的值"""
    resultText = input(inputText)
    # 如果用户输入了内容，则直接返回结果
    if len(resultText) > 0:
        return resultText
    # 如果用户没有输入内容，则返回字典中原有的值
    else:
        return dictValue
