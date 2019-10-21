#父类Master
class Master(object):
    def __init__(self):
        self.kongfu="白马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

#父类School
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
        self.__init__()
        print(f"使用{self.kongfu}制作果子")

    #调用父类Master的同名的方法和属性
    def makeMasterCake(self):
        Master.__init__(self)
        Master.makeCake(self)
    #调用父类School的同名的方法和属性
    def makeSchoolCake(self):
        School.__init__(self)
        School.makeCake(self)

#创建对象daqiu
daqiu=Prentice()

#调用子类的方法
daqiu.makeCake()

#调用父类Master的方法
daqiu.makeMasterCake()

#调用父类School的方法
daqiu.makeSchoolCake()

#调用子类的方法
daqiu.makeCake()