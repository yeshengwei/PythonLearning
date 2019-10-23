try:
    f=open("test.txt","r")

except Exception as result:
    f=open("test.txt","w")

else:
    print("无异常")

finally:
    f.close()

