import functools
list1=[1,2,3,4,5,6]

def func1(x,y):
    return x+y

print(functools.reduce(func1,list1))