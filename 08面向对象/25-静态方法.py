class Dog(object):
    @staticmethod
    def infoPrint():
        print("这是静态方法...")

#创建对象
xiaohei=Dog()

#对象调用静态方法
xiaohei.infoPrint()


#类调用静态方法
Dog.infoPrint()