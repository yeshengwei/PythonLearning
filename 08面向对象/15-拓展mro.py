#父类
class Master(object):
    def __init__(self):
        self.kongfu="白马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

#父类
class School(object):
    def __init__(self):
        self.kongfu="黑马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

#子类
class Prentice(School,Master):
    def __init__(self):
        self.kongfu="独创煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

#创建对象
daqiu=Prentice()
#调用对象属性
print(daqiu.kongfu)
#调用对象方法
daqiu.makeCake()

print(Prentice.__mro__)


