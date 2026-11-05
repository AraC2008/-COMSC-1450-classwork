import math
'''
x1=3
y1=5
x2=7
y2=8
print(math.sqrt(math.pow(x1-x1,2)+math.pow(y2-y1,2)))
'''
'''
a = int(input("Give me an angle: "))
conv = math.radians(a)
print(math.sin(conv))
print(math.cos(conv))
'''
'''
import random
print(random.random())
print(random.choice("ABCDEF"))
print(random.randint(1,50))
'''
'''
def show_welcome_banner():
    print("***************************\nWelcome to Python Programming!\n***************************")
show_welcome_banner()
show_welcome_banner()
show_welcome_banner()

'''
'''
def greet_user(x):
    print("Hello", x,"welcome back!")
x = input("what is your name: ")
greet_user(x)
'''
'''
def Even_odd(x):
    if (x%2==0):
         print("Number is even")
    else:
         print("Number is odd")
x = int(input("Enter a number: "))
Even_odd(x)
'''
'''
def dollars_to_euros(X):

    u = X * 0.92
    return u
print(dollars_to_euros(50))
'''
'''
def calculate_shipping(X,Y):
    m=X*0.50
    m2= Y*0.10
    return m + m2
print("$" ,calculate_shipping(12,250))
'''
'''
def vowels(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count = count + 1
    return count
print(vowels("Houston"))
'''
'''
def get_rectangle (x,y):
    Area = x * y
    return Area
print(get_rectangle(5,6))
'''
'''
def maximum (a,b):
    if a > b:
        return (a)
    else:
        return(b)

print(maximum(9,4))
'''
'''
def is_even (n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(6))
'''
'''
import math
def circle_area(radius):
    Area = math.pi * radius**2
    return Area
print(circle_area(4))
'''

'''
def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n-1)      
'''
