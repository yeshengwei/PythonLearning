class Dog(object):
    tooth=10


wangcai=Dog()
xiaohei=Dog()

#通过类修改：类.类属性=值
Dog.tooth=10000
print(Dog.tooth)


#对象调用类属性
print(wangcai.tooth)
print(xiaohei.tooth)


#通过对象修改类属性
wangcai.tooth=20000000

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

#不能通过对象修改，通过对象修改表示是创建了与类属性同名的实例属性