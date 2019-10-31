class Person():
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight


    def run(self):
        print(f"我的名字是{self.name},体重是{self.weight}公斤。")
        self.weight-=0.5

    def eat(self):
        print(f"我的名字是{self.name},体重是{self.weight}公斤。")
        self.weight+=0.5

xiaoming=Person("小明",75)
xiaoming.eat()
xiaoming.run()


xiaomei=Person("小美",45)
xiaomei.eat()
xiaomei.run()


