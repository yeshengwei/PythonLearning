from student import *


# 一、定义管理系统类
class StudentManager():
    def __init__(self):
        self.studentlist = []

    def run(self):
        # 加载文件里面学员信息
        self.loadStudent()

        while True:
            # 显示系统功能菜单
            self.showMenu()

            # 用户输入功能菜单
            menunum = int(input("请选择您需要的功能："))

            # 根据用户输入执行不同的功能
            if menunum == 1:
                self.addStudent()
            elif menunum == 2:
                self.delStudent()
            elif menunum == 3:
                self.modifyStudent()
            elif menunum == 4:
                self.searchStudent()
            elif menunum == 5:
                self.showStudent()
            elif menunum == 6:
                self.saveStudent()
            elif menunum == 7:
                break

    # 二、系统功能函数
    # 显示功能菜单
    @staticmethod
    def showMenu():
        print("***请选择功能选项：***")
        print("1.添加学员信息")
        print("2.删除学员信息")
        print("3.修改学员信息")
        print("4.查询学员信息")
        print("5.显示所有学员")
        print("6.保存学员信息")
        print("7.退出管理系统\n")

    # 添加学员信息
    def addStudent(self):
        name = input("请输入学员姓名：")
        gender = input("请输入学员性别：")
        tel = input("请输入学员电话：")
        student = Student(name, gender, tel)
        self.studentlist.append(student)
        print("学员添加已完成！")

    # 删除学员信息
    def delStudent(self):
        delName = input("请输入需要删除学员的姓名：")
        for i in self.studentlist:
            if i.name == delName:
                self.studentlist.remove(i)
                print(f"学员信息删除成功!姓名是:{i.name},性别是:{i.gender},电话是:{i.tel}。")
                break
        else:
            print("学员不存在，请重新输入！")

    # 修改学员信息
    def modifyStudent(self):
        modifyName = input("请输入需要修改学员的姓名：")
        for i in self.studentlist:
            if i.name == modifyName:
                i.name = input("请输入学员姓名：")
                i.gender = input("请输入学员性别：")
                i.tel = input("请输入学员电话：")
                print(f"学员信息修改成功!姓名是:{i.name},性别是:{i.gender},电话是:{i.tel}。")
                break
            else:
                print("学员不存在，请重新输入！")

    # 查询学员信息
    def searchStudent(self):
        searchName = input("请输入需要修改学员的姓名：")
        for i in self.studentlist:
            if i.name == searchName:
                print(f"学员信息已找到，姓名是:{i.name},性别是:{i.gender},电话是:{i.tel}。")
                break
        else:
            print("学员不存在，请重新输入！")

    # 显示所有学员信息
    def showStudent(self):
        print("姓名\t\t性别\t\t电话")
        for i in self.studentlist:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    # 保存学员信息
    def saveStudent(self):
        # 打开文件
        f = open("student.data", "w")
        # 写入数据
        newList = [i.__dict__ for i in self.studentlist]
        # 文件写入
        f.write(str(newList))
        # 关闭文件
        f.close()
        print("学员信息已保存成功！")

    # 加载学员信息
    def loadStudent(self):
        # 尝试以只读模式打开文件
        try:
            f = open("student.data", "r")
        # 如果文件不存在，则创建文件
        except:
            f = open("student.data", "w")
        # 读取数据
        else:
            data = f.read()
            newList = eval(data)
            self.studentlist = [Student(i["name"], i["gender", i["tel"]]) for i in newList]
        # 关闭文件
        finally:
            f.close()
