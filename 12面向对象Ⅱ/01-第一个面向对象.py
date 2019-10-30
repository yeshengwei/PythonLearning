class Cat():
    """定义一个猫类"""

    def eat(self):
        """定义一个吃方法"""
        print("小猫爱吃鱼..")

    def drink(self):
        """定义一个喝方法"""
        print("小猫爱喝水..")


# 通过Cat类创建对象tom
tom = Cat()

# tom调用吃方法
tom.eat()

# tom调用喝方法
tom.drink()

print(tom)

addr = id(tom)
print("%x" % addr)
