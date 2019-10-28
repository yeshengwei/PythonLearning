import cards_tools
while True:
    #调用显示菜单函数
    cards_tools.showMenu()

    action=input("请输入您要选择的功能：")
    print("您选择的操作是[%s]"%action)

    #接收用户输入
    if action in ["1","2","3"]:
        #新增名片
        if action=="1":
            cards_tools.addCard()
        #显示全部
        elif action=="2":
            cards_tools.showCard()
        #查询名片
        elif action=="3":
            cards_tools.searchCard()

    #退出系统
    elif action=="0":
        print("欢迎再次使用名片管理系统！")
        break
    #输入错误
    else:
        print("输入错误，请重新输入！")