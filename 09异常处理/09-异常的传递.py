import time
try:
    f=open("test.txt")
    #尝试循环读取内容
    try:
        while True:
            result=f.readline()
            if len(result)==0:
                break
            time.sleep(2)
            print(result)
    except:
        print("用户终止")

    finally:
        f.close()
        print("文件关闭")


except:
    print("没有这个文件")
