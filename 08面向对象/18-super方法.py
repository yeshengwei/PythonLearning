#父类Master
class Master(object):
    def __init__(self):
        self.kongfu="白马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

#父类School
class School(Master):
    def __init__(self):
        self.kongfu="黑马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

        #使用super有参数方法调用父类
        # super(School,self).__init__()
        # super(School,self).makeCake()

        #使用super无参数方法调用父类
        super().__init__()
        super().makeCake()


class Prentice(School):
    def __init__(self):
        self.kongfu="独创煎饼果子配方"


    def makeCake(self):
        self.__init__()
        print(f"使用{self.kongfu}制作果子")


    #调用父类Master的同名的方法和属性
    # def makeMasterCake(self):
    #     Master.__init__(self)
    #     Master.makeCake(self)
    # #调用父类School的同名的方法和属性
    # def makeSchoolCake(self):
    #     School.__init__(self)
    #     School.makeCake(self)

    #方法1：一次性调用父类同名的属性和方法
    def makeOldCake(self):
        # Master.__init__(self)
        # Master.makeCake(self)
        # School.__init__(self)
        # School.makeCake(self)

    #方法2：使用super有参数方法
        # super(Prentice, self).__init__()
        # super(Prentice,self).makeCake()
    # 方法2：使用super无参数方法
        super().__init__()
        super().makeCake()

daqiu=Prentice()
daqiu.makeOldCake()