class Father():
    def __init__(self):
        self.num=1

    def infoPrint(self):
        print(self.num)


#子类继承父类
class Soon(Father):
    pass




#通过子类创建对象
result=Soon()

#对象调用方法
result.infoPrint()