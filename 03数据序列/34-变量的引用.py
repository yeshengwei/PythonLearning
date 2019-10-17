# x=22
# y=x
#
# print(id(x))
# print(id(y))
#
# x=100
#
# print()
#

x = [3, 100, 9]
y = x

print(id(x))
print(id(y))

x.append("44")

print(x)
print(y)
