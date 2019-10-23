try:
    print(num)

except (ZeroDivisionError,NameError) as result:
    print(result)