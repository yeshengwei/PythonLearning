class Master(object):
    def __init__(self):
        self.kongfu="煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

class Prentice(Master):
    pass


daqiu=Prentice()
daqiu.makeCake()