# 定义家具类
class Furniture():
    # 初始化
    def __init__(self, name, area):
        self.name = name
        self.area = area


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.freeArea = area
        # 家具列表
        self.furniture = []

    def addFurniture(self, item):
        """容纳家具"""
        if item.area < self.freeArea:
            self.furniture.append(item.name)
            self.freeArea -= item.area

        else:
            print("家具太大无法放入！")

    # 查看对象
    def __str__(self):
        return f"房屋的地理位置在{self.address},房屋的面积为{self.area},剩余面积为{self.freeArea},房屋的家具有{self.furniture}。"


# 创建家具对象
shafa = Furniture("沙发", 10)
chuang = Furniture("单人床", 50)
zhuozi = Furniture("桌子", 100)

# 创建家对象
home1 = Home("苏州", 100)
print(home1)

home1.addFurniture(shafa)
print(home1)

home1.addFurniture(zhuozi)
print(home1)

home1.addFurniture(chuang)
print(home1)