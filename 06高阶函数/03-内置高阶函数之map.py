list1=[1,2,3,4,5,6]

def func1(x):
    return x**2


result=map(func1,list1)
print(list(result))