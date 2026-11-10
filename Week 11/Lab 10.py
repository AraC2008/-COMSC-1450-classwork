'''
while True:
    try:
        numerator = int(input("Enter a number for the numerator"))
        denomenator = int(input("Enter a number for the denominator"))
        safe_divide=(numerator/denomenator)
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(safe_divide)
        break
'''
'''
try:
    list_cart= ["Laptop", "Headphones", "Backpack", "Water Bottle"]
    x = int(input("Enter the item you want to view: "))
    print(list_cart[x])
except ValueError:
    print("Enter a number this is a word")
except IndexError:
    print("Please enter a number in range")
except Exception as e:
    print(e)
'''
'''
f=  open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\Week 11\\grades.txt","r")

try:
    total = 0
    for i in f:
        total += int(i)
    
except FileNotFoundError:
    print("No file found")
except ValueError:
    print("data courruption, you didn't enter a number")
else:
    print(total)
finally:
   f.close()
'''














'''
try:
    variableaccount_balance=500
    x = int(input("Enter withdrawl amount: "))
    if x <= 0:
        raise ValueError("Withdrawl must be greater than zero")
    if x > variableaccount_balance:
        raise ValueError("Insufficient funds available")
except Exception as e:
    print(e)
else:
    print(variableaccount_balance - x)
'''
