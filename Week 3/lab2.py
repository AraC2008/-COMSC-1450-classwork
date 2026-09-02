'''
x = input("Give me a number:")
if (x>0):
    print("You have a positive number")
if (x<0):
    print("You have a negative number")
'''
'''
x =int(input("Give me a number:"))
if(x % 2 == 0):
    print("even")
else:
    print("Odd")
'''
'''
x=int(input("what is your age?:"))
if(x<19):
    print("Teenager")
else:
    print("Adult")
'''
'''
x =int(input("What is the temperatue?:"))
if(x>80):
    print("Hot")
else:
    print("Not hot")
'''
'''
x = int(input("Give me x:"))
y = int(input("Give me y:"))
if(x>y):
    print("The larger is", x)
else:
    print("The larger is", y)
'''
'''
x = int(input("Give me your score: "))
if(x>0 and x<=100):
    print("Valid")
else:
    print("Invalid")
'''
'''
x = int(input("Give me x:"))
y = int(input("Give me y:"))
if(x==y):
    print("Equal")
else:
    print("Different")
'''
'''
x = int(input("Enter your PIN:"))
if(x==1234):
    print("Access granted")
else:
    print("Access denied")
'''
'''
x = int(input("What is the temperature?:"))
if(x>=100):
   print("Very hot")
elif(x>=80 and x<100):
   print("Hot")
elif(x>=60 and x<79):
   print("Warm")
elif(x<60):
   print("Cold")
'''
'''
x = int(input("Give me your grade:"))
if(x>90):
    print("A")
elif(x>80 and x<89):
    print("B")
elif(x>70 and x<79):
    print("C")
elif(x>60 and x<69):
    print("D")
elif(x<60):
    print("F")
'''
'''
x = int(input("Give me x:"))
y = int(input("Give me y:"))
z = int(input("Give me z:"))
if(x>y and x>z):
    print(x, " is the greatest")
elif(y>x and y>z):
    print(y,"is greatest")
elif(z>x and z>y):
    print(z,"is the greatest")
'''
'''
x = int(input("What is your age?"))
if(x<13):
    print("$5")
elif(x>13 and x<17):
    print("$8")
elif(x>18 and x<65):
    print("$12")
elif(x>65):
    print("$7")
'''
'''
x = int(input("give me number 1: "))
y = int(input("Give me number 2: "))
op = input("give me an operator(+,-,*,/):")
if(op =="+"):
    print(x+y)
elif(op =="-"):
    print(x-y)
elif(op=="*"):
    print(x*y)
elif(op =="/"):
    print(x//y)
'''