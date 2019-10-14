name_list=["lily","tom","rose","will"]
del name_list[1]
print(name_list)


del_name_list=name_list.pop(1)
print(del_name_list)
print(name_list)


name_list.remove("will")
print(name_list)

name_list.clear()
print(name_list)