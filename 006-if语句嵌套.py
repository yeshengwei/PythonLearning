money = int(input("请输入你带的人民币金额："))
seat = int(input("请输入是否有空座："))
if money == 1:
    print("可以上车")
    if seat == 1:
        print("有空座，请坐下")
    else:
        print("无空座，请站好")
else:
    print("没钱不能上车")