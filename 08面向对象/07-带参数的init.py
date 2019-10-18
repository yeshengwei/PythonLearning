class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def printInfo(self):
        print(f"宽度{self.width}")
        print(f"高度{self.height}")


# 创建对象1
haier1 = Washer(100, 200)
haier1.printInfo()

# 创建对象2
haier2 = Washer(1, 2)
haier2.printInfo()

# 创建对象3
haier3 = Washer(4, 100)
haier3.printInfo()
