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

#孙类
class Sun(Prentice):
    pass

#创建对象xiaoqiu
xiaoqiu=Sun()
xiaoqiu.makeCake()
xiaoqiu.makeMasterCake()
xiaoqiu.makeSchoolCake()
