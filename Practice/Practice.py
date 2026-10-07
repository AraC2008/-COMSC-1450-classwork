'''
name = input("Enter your name: ")
print("Welcome to the course,",name,"!")
'''
'''
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print("Hello", last_name, ",", first_name)
'''
'''
x = 32
y = "sara"
z = 3.5
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
item_class = "Electronics" 
item_Age = 2 
print("Printing details")
print(first_item, total_cost,item_class)
print("Item age is:", item_Age)
'''
'''
length = int(input("Enter the length: "))
width = int(input("Enter the width:"))
Area = length * width
print(Area)
'''
'''
name = input("Enter your name: ")
budget = int(input("Enter monthly budget($): "))
daily_cost = float(input("Enter daily food cost($): "))
total_cost = daily_cost * 30
remaining = budget - total_cost
print("--- BUDGET SUMMARY --- \n", name,"|","Food:$",total_cost,"|","Remaining:", remaining)
'''
'''
r = float(input("Enter the radius: "))
Pi = 3.14159
Area = Pi*r**2
print(Area)
'''
'''
t = float(input("Enter the temperature in Celsius: "))
F = (t*(9/5)+32)
print(F,"is the temperature in fahrenheit")
'''
'''
x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))
z = float(input("Enter number 3: "))
average = (x + y + z)/3
print("Average =",average)
'''
'''
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
print("before:")
print("x=", x)
print("y=",y)
temp = x
x = y
y = temp
print("After:")
print("x=", x)
print("y=",y)
'''
'''
O = int(input("What is the original price: "))
D = float(input("What is the discount percentage: "))
T = float(input("Enter the tax percentage: "))
x = O * D/100
y = O - x
z = y * T/100
final_price = y + z
print(final_price)
'''