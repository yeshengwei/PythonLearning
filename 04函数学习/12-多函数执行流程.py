globalNum = 5


def func1():
    global globalNum
    globalNum = 200
    print(globalNum)


def func2():
    print(globalNum)


func2()
func1()
func2()
