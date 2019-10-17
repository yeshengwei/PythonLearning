# y=1000000000
#
# def func1(x):
#     print(x)
#     print(id(x))
#     x+=x
#     print(id(x))
#
# func1(y)

y = [1, 2, 3, 4, 5, 6]


def func1(x):
    print(x)
    print(id(x))
    x += x
    print(id(x))


func1(y)
