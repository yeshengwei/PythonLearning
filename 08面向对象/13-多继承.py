class Master(object):
    def __init__(self):
        self.kongfu="白马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")


class School(object):
    def __init__(self):
        self.kongfu="黑马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")


class Prentice(School,Master):
    pass


daqiu=Prentice()
print(daqiu.kongfu)
daqiu.makeCake()
