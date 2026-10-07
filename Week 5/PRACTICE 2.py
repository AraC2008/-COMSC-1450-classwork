'''
x = input("What is your name: ")
print("Welcome to the course," , x,"!")
'''
'''
f = input("First name: ")
l = input("Last name: ")
print("Hello",l,",",f)
'''
'''
x=32
y="sara"
z=3.5
print(type(x))
print(type(y))
print(type(z))
'''
'''
print("A\nB\nC\nD\nE\nF")
'''
'''
file_path = print("C:\\Users\\rick\\Documents")
print("--- SYSTEM MENU ---\n1. Open File\n2. Save File\nThe professor said,'Make sure you escape matching quotes!'")
'''
'''
first_item = "Keyboard"
total_cost = 45.00 
category = "Electronics" 
item_Age = 2 
print(first_item, total_cost, category,"Item age is:", item_Age)
'''
'''
l = int(input("Enter the length: "))
w = int(input("Enter the width: "))
Area = l * w
print(Area)
'''
'''
name = input("Enter your name: ")
budget = int(input("Enter monthly budget($): "))
daily =float(input("Enter daily food cost($): "))
monthly_cost = daily * 30
remaining = budget - monthly_cost
print(name,"|","Food:$",monthly_cost,"|","Remaining:$",remaining)
'''
'''
r= float(input("Enter the radius: "))
Pi = 3.14159
Area=Pi*r**2
print(Area)
'''
'''
C =float(input("Enter the temperature in celcius: "))
F = (C*(9/5)+32)
print(F)
'''
'''
x = int (input("Enter number 1: "))
y= int(input("Enter number 2: "))
z = int (input("Enter number 3: "))
average =(x+y+z)/3
print("Average =", average)
'''
'''
x = 10
y = 20
placer = x
x=y
y = placer
print( x , y )
'''
'''
O = int(input("Enter the original price: "))
D = float(input("Enter the discount percentage: "))
T = float(input("Enter the tax percentage: "))
discount_conversion= O * (D/100)
after_discount= O - discount_conversion # had trouble with the equations
tax_conversion= after_discount*(T/100)
after_tax= after_discount + tax_conversion
print("Final price = ",after_tax)
'''
'''
A= 10
B= 20
C= 30
placer = A
A = B
B = C
C = placer
print(A,B,C)
'''
'''
x=5
y=15
z=25
placer = x
x=z
z=y
y = placer
print(x,y,z)
'''
'''
x= int(input("Enter a number: "))
if(x<0):
    print("Negative")
else:
    print("Positive")
'''
'''
x= int(input("Enter a number : "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
'''
'''
x= int(input("Enter your age: "))
if (x<=19):
    print("Teenager")
else:
    print("Adult")
'''
'''
x = int(input("What is the temerature: "))
if(x>80):
    print("Hot")
else:
    print("Not hot")
'''
'''
X_one = int(input("Enter a number: "))
X_two = int(input("Enter a number: "))
if X_one > X_two:
    print(X_one,"is larger")
elif X_two > X_one:
    print(X_two,"is larger") # i had a bit of trouble on this one
else:
    print("Numbers are equal")
'''
'''
x= int(input("Enter your score: "))
if (x>0) and (x<100):
    print("Valid score")
else:
    print("invalid score")
'''
'''
num_1 = float(input("Enter number 1: "))
num_2 = float(input("Enter number 2: "))
if num_1 == num_2:
    print("Same")
else:
    print("Different")
'''
'''
PIN = 1234
x = int(input("Enter your password: "))
if x == PIN:
    print("Access granted")
else:
    print("Access denied")
'''
'''
x = int(input("What is the temperature: "))
if x > 100:
    print("Very hot")
elif x > 80 and x < 100:
    print("Hot")
elif x > 60 and x < 79:
    print("Warm")
else:
 print("Cold")
 '''
'''
x = int(input("Enter your grade: "))
if x > 90:
    print("A")
elif x>80 and x<89:
    print("B")
elif x>70 and x<79:
    print("C")
elif x>60 and x<69:
    print("D")
else:
    print("F")
'''
'''
num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
num_3 = int(input("Enter number 3: "))
if num_1 > num_2 and num_1 > num_3:
    print(num_1,"is the largest")
elif num_2 > num_1 and num_2 > num_3:
    print(num_2,"is the largest")
else:
    print(num_3,"is the largest")
'''
'''
x = int(input("Enter your age: "))
if x > 65:
    print("$7")
elif  x > 18:
    print("$12")
elif x > 13:
    print("$8")
else:
    print("$5")
'''
'''
num_1 = int(input("Enter number 1: "))
num_2 = int(input("ENter number 2: "))
O = input("Enter an operator (+,-,*,/): ")
if O == "+":
    print(num_1+num_2)
elif O == "-":
    print(num_1-num_2)
elif O == "*":
    print(num_1*num_2)
elif O == "/":
    print(num_1/num_2)
'''
'''
x=0
while (x<10):
    x = x + 1
      print(x)
'''
'''
X=0
while X<20:
    X = X + 2
    print(X)
'''
'''
x= int(input("Enter your starting number: "))
while x >=0:
    print(x)
    x-=1 # need to better understand these types of equations
'''
'''
for x in range(2,31,2):
    print(x,x**2)
'''
'''
Correct_password= "STTHOM"
x = input("Enter your password: ")
while x!= Correct_password:
    print("Wrong password, try again")   # Had trouble with this one
    x = input("Enter your password: ")
'''
'''
x = 76
while True:
    User_guess=int(input("Guess a number 1-100: "))
    if User_guess == x:
        print("Correct")
        break                   # this one too
    elif User_guess < x:
        print("Too low")
    else:
        print("Too high")
'''
