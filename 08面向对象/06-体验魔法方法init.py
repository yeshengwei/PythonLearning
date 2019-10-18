class Washer():
    def __init__(self):
        self.width = 100
        self.height = 200

    def printInfo(self):
        print(f"宽度是{self.width}")
        print(f"高度是{self.height}")


# 创建对象
haier = Washer()

# 调用对象方法
haier.printInfo()
