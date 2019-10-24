class A():
    a = 0

    def __init__(self):
        self.b = 0


aa = A()

# 类调用__dict__
print(aa.__dict__)

# 对象调用__dict__
print(A.__dict__)
