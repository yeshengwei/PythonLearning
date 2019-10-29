# 定义学员类
class Student(object):
    # 定义学员类的属性
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"{self.name},{self.gender},{self.tel}"
