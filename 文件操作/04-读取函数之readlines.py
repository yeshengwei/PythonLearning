file=open("test.txt","r")

list=(file.readlines())
for i in list:
    print(i)


file.close()