func = lambda *args: args
print(func(1, 2, 3, 4, 5, 6, 7))

print(func(1, 2, 7))

print(func(1, ))

func2 = lambda **kwargs: kwargs
print(func2(name="rose", age=19, add="suzhou"))
