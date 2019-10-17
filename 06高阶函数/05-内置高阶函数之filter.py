list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func1(x):
    return x % 2 == 0


print(list(filter(func1, list1)))
