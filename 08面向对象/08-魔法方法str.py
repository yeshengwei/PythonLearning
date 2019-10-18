class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Washer"

    def printInfo(self):
        print(f"宽度{self.width}")
        print(f"高度{self.height}")

    def __del__(self):
        print("对象1已被删除")


# 创建对象1
haier1 = Washer(100, 200)
print(haier1)
