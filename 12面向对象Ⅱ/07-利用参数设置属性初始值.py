class Cat():
    def __init__(self, name):
        print("这是一个初始化方法...")

        # 添加name属性
        self.name = name

    def eat(self):
        print("%s爱吃鱼.." % self.name)


# 使用类名创建对象时，会自动调用初始化方法init
tom = Cat("TOM")
print(tom.name)
tom.eat()

lazyCat = Cat("lazyCat")
print(lazyCat.name)
lazyCat.eat()
