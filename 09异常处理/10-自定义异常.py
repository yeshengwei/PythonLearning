#自定义异常类
class ShortInputError(Exception):
    def __init__(self,length,minlen):
        self.length=length
        self.minlen=minlen

#设置异常描述信息
    def __str__(self):
        return f"你输入的密码长度是{self.length}个字符,不能少于{self.minlen}个字符。"


def main():
    try:
        password=input("请输入密码：")
        if len(password)<3:
            raise ShortInputError(len(password),3)

    except Exception as result:
        print(result)

    else:
        print("密码输入完成，没有异常！")


main()