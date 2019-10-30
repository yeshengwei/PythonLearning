class Cat():
    def __init__(self, name):
        self.name = name

        print("%s来了.." % self.name)

    def __del__(self):
        print("%s走了.." % self.name)

    def __str__(self):
        return "我是小猫..."


tom = Cat("Tom")
print(tom)
