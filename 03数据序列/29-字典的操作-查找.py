dict1={"name":"yeshengwei","age":19,"address":"suzhou"}
"""
#通过key查找
print(dict1["age"])
print(dict1["abc"])

#通过函数查找
print(dict1.get("name"))
print(dict1.get("names","lily"))
print(dict1.get("names"))
"""
print(dict1.keys()) #查找字典中所有的key

print(dict1.values()) #查找字典中所有的value


print(dict1.items())