age = int(input("请输入你的年龄："))
if age < 18:
    print(f"你的年龄为{age},不能工作")
elif (age >= 18) and (age <=60):
    print(f"你的年龄为{age},合法工作")
elif age > 60:
    print(f"你的年龄为{age},请退休")