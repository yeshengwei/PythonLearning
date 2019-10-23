try:
    print(1/0)

except (ZeroDivisionError,NameError):
    print("代码有异常")