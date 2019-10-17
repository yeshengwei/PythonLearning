# 函数自己调用自己
# 必须有出口

def sumNumbers(num):
    if num==1:
        return 1
    return num+sumNumbers(num-1)

result=sumNumbers(10)
print(result)

print("test")

