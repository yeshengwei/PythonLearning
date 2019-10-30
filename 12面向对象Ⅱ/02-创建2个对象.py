class Cat():
    """定义一个猫类"""

    def eat(self):
        """定义一个吃方法"""
        print("小猫爱吃鱼..")

    def drink(self):
        """定义一个喝方法"""
        print("小猫爱喝水..")


tom = Cat()
tom.eat()
tom.drink()
print(tom)

lazyCat = Cat()
lazyCat.eat()
lazyCat.drink()
print(lazyCat)

lazyCat2 = lazyCat
print(lazyCat2)
