class Dog(object):
    __tooth=10

    @classmethod
    def getTooth(cls):
        return cls.__tooth



wangcai=Dog()
print(wangcai.getTooth())