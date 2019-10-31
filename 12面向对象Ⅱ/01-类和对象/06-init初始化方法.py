class Cat():
    def __init__(self):
        print("这是一个初始化方法...")

        # 添加name属性
        self.name = "Tom"

    def eat(self):
        print("%s爱吃鱼.." % self.name)


# 使用类名创建对象时，会自动调用初始化方法init
tom = Cat()

print(tom.name)

tom.eat()
