'''
def Add(x):
    count = 0
    for i in range(x):
        count = count + i
        print(count)
Add(10P)
'''
'''
def countdown (n):
     if n == 0:
         return
     print(n)
     countdown(n-1)
countdown(5)  
'''
'''
def factorial (n):
    if n == 0:
        return 1
    return n * factorial(n-1)      
'''
'''
def sum (n):
    if n == 0:
        return n
    return n+ sum(n-1)
sum(5)
'''
'''
list = [2,4,6,8,10]
odd=0
even= 0
for i in list:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers:", even)
print("Odd numbers:", odd)  
'''
'''
list2=[]
list = [2,3,4,3,5,6]
for i in list:
    if i not in list2:
        list2.append(i)
print("List without duplicates:", list2)
'''
'''
listx=[1,2,3,4,5]
listy=[6,7,8,9,10]
listz=[]
listz.extend(listx)
listz.extend(listy)
print("Concatenated list:", listz)
'''
'''
list=[1,2,3,-4,-5,-6,7,-8,9,-10]
positive=[]
negative=[]
for i in list:
    if i > 0:
        positive.append(i)
    else:
        negative.append(i)
print("Positive numbers:", positive)
print("Negative numbers:", negative)
'''
'''
list = ["python", "texas","pie", "she", "hi"]
for i in list:
    if len(i) > 4:
        print(i)
'''
'''
list = [2,4,3,5,6,7,8,9]
squaered_list = [i**2 for i in list]
print("Squared list:", squaered_list)
'''

'''
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week6\\Week7\\textfile.txt","w")
file.write("Hello, python\n")
file.write("Welcome , 2026!\n")
file.write("UST\n")
file.close()
'''
'''
name=input("Enter your name: ")
file = open("C:\\Users\\araco\\OneDrive\\Documents\\COMSC 1450\\-COMSC-1450-classwork\\Week6\\Week7\\textfile.txt","a")
file.write(name)
file.close()
'''