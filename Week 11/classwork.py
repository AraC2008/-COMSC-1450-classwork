'''
try:
    x = int(input("Enter your age: "))
    if x <= 0:
        raise ValueError("Enter valid age")
except ValueError as e:
    print(e)
else:
    print("your age is ", x)
'''
'''
try:
    f=  open("data.txt","r")
    total = 0
    for i in f:
        total += int(i)
    print(f.read())
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
finally:
    f.close()
'''
