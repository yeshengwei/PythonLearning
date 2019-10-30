class Cat():
    """定义一个猫类"""

    def eat(self):
        # 哪个对象调用的方法，self就是哪一个对象的引用
        """定义一个吃方法"""
        print("小猫爱吃鱼..")

    def drink(self):
        """定义一个喝方法"""
        print("小猫爱喝水..")


# 创建对象
tom = Cat()

# 添加对象属性
tom.name = "Tom"

tom.eat()
tom.drink()

print(tom.name)
