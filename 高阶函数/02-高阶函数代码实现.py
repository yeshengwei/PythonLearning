def sumNum(x,y,f):
    return f(x)+f(y)

print(sumNum(-3,4.6,round))
print(sumNum(-3,4.6,abs))