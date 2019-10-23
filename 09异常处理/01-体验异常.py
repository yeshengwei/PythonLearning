#可能发生错误的代码
try:
    open("text.txt","r")


#如果发生错误后执行的代码
except:
    print("代码执行错误，请检查！")