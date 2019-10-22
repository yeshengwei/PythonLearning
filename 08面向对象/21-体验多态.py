#定义狗类
class Dog(object):
    #定义父类的公共方法
    def work(self):
        print("指哪打哪...")

#定义狗的子类
class ArmyDog(Dog):
    def work(self):
        print("追击敌人...")

#定义狗的子类
class DrugDog(Dog):
    def work(self):
        print("追查毒品...")


#定义人类
class Person(object):
    def workWithDog(self,dog):
        dog.work()

#创建对象
ad=ArmyDog()
dd=DrugDog()

police=Person()
#调用相同的方法，传入不同的参数，执行不同的功能
police.workWithDog(ad)
police.workWithDog(dd)
