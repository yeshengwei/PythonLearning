
a=100
print(a)

def testA():
    print(a)

def testB():
    global a
    a=200
    print(a)

testA()
testB()
print(a)
