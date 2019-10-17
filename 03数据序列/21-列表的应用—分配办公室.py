#8位老师分配到3个办公室
import random
teachers=["li","ye","zhang","wang","zhou","huang","xie","wei"]
offices=[[],[],[]]
for i in teachers:
    num=random.randint(0,2)
    offices[num].append(i)
o = 1
for office in offices:
    print(f"办公室{o}的人数是{len(office)},老师的名字分别是：")
    for name in office:
        print(name)

    o+=1