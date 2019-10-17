student = [
    {"name": "rose", "age": 20, "add": "sz"},
    {"name": "tom", "age": 30, "add": "sz"},
    {"name": "jack", "age": 90, "add": "sz"}
]

student.sort(key=lambda x: x["name"])
print(student)

student.sort(key=lambda x: x["age"], reverse=True)
print(student)

student.sort(key=lambda x: x["age"])
print(student)
