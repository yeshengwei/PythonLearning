class Cat():
    def eat(self):
        print("%s爱吃鱼.." % self.name)

    def drink(self):
        print("%s爱喝水.." % self.name)


xiaohei = Cat()
xiaohei.name = "Xiaohei"

xiaohei.eat()
xiaohei.drink()

tom = Cat()
tom.name = "Tom"

tom.eat()
tom.drink()
