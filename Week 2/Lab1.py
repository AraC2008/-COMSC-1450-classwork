'''
name = input("Enter your name: ")
print("Welcome to the course, " + name + "!")
'''
'''
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, " + last_name + ", " + first_name)
'''
'''
x = 32
y = "Sara"
z = 3.5
print(int(x)) , print(str(y)) , print(float(z))
'''
'''
print("A\nB\nC\nD\nE\nF")
'''
'''
file_path = print('C:\\Users\\rick\\Documents\n''''--- SYSTEM MENU ---''''\n1. Open File\n2. Save File')
print("The professor said, 'Make sure you escape matching quotes!'")
'''
'''
first_item = "Keyboard" 
total_cost = 45.00
item_class = "Electronics"
item_Age = 2
print(first_item, total_cost, item_class, "Item age is:", item_Age)
'''
'''
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
area = length * width
print("The area of the rectangle is:", area)
'''
'''
name= input("Enter your name: ")
monthly_budget = float(input("Enter monthly budget ($): "))
daily_food_cost = float(input("Enter daily food cost ($): "))
print("--- BUDGET SUMMARY ---\n", name, "|", daily_food_cost * 30, "|", daily_food_cost * 30 - monthly_budget)
'''
'''
Pi = 3.14
r = float(input("What is the radius of the circle?: "))
Area = Pi*r**2
print (Area)
'''
'''
c = float(input("What is the temperature in celsius?: "))
F=(c*(9/5)+32)
print("The temperature in farenheit is,", F )
'''
'''
x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))
z = float(input("Enter number 3: "))
total = (x + y + z) / 3
average = (total)
print("Average =" , total)
'''
'''
x = 5
y = 7
temp = x
x = y
y = temp
print(x,y)
'''
'''
price = float(input("Original price: "))
discount = float(input("discount percentage: "))
tax = float(input("tax percdentage :"))
discount_amount = price * discount/100
price_after_discount = price - discount_amount
price_after_tax = price_after_discount *tax/100
final_price =price_after_discount - price_after_tax
print(final_price)
'''