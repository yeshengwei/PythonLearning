class SweetPotato():
    def __init__(self):
        self.cookTime = 0
        self.cookState = "生的"
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        self.cookTime += time
        if 0 <= self.cookTime < 3:
            self.cookState = "生的"
        elif 3 <= self.cookTime < 5:
            self.cookState = "半生不熟"
        elif 5 <= self.cookTime < 8:
            self.cookState = "熟的"
        elif self.cookTime >= 8:
            self.cookState = "烤糊了"

    def addCondiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f"这个地瓜烤了{self.cookTime},状态是{self.cookState},添加的调料有{self.condiments}。"


# 创建对象
sweetpotato1 = SweetPotato()
# 打印对象
# print(sweetpotato1)

# 对象调用类的cook方法,并且传参数time进去
sweetpotato1.cook(3)

# 对象调用类的addCondiments方法,并且传参数condiment进去
sweetpotato1.addCondiments("孜然")
print(sweetpotato1)

sweetpotato1.cook(3)
sweetpotato1.addCondiments("辣椒面")
print(sweetpotato1)
