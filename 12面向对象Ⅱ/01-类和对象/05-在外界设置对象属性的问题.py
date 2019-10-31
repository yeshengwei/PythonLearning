class Cat():
    def eat(self):
        print("%s爱吃鱼.." % self.name)

    def drink(self):
        print("%s爱喝水.." % self.name)


xiaohei = Cat()

xiaohei.eat()
xiaohei.drink()

# 移动代码顺序后运行即会报错，所以一般把属性封装在类的内部
xiaohei.name = "Xiaohei"
