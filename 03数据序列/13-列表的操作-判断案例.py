name_list=["Tom","Will","Jack","Rex"]
name=input("请输入您的姓名：")
#print(f"您输入的姓名是{name}")
if name in name_list:
    print("您输入的用户名在系统中已存在，请重新输入。")
else:
    print(f"您的账号{name}注册成功！")