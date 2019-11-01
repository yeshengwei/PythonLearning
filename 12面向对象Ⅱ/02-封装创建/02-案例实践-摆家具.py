# 创建房子类
class HouseItem():
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"[{self.name}]占地[{self.area}]平米。"


# 创建家具类
class House():
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f"户型：[{self.house_type}]\n总面积：[{self.area}]\n剩余面积[{self.free_area}]\n家具：[{self.item_list}]"

    # 添加家具方法
    def add_item(self, item):
        # 判断家具的面积
        if item.area > self.area:
            print(f"{item.name}的面积太大了，无法添加！")
            return

        # 将家具的名称添加到列表中
        self.item_list.append(item.name)

        # 计算剩余面积
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 3)
table = HouseItem("餐具", 1.5)

# 创建房子对象
my_home = House("两室一厅", 100)

# 添加家具
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
