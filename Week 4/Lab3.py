'''
C = 1
while(C<=10):
    print(C)
    C= C + 1
'''
'''
C=2
while(C<=20):
    print(C)
    C = C + 2
'''
'''
C = int(input("Give me a number: "))
while(C>=0):
    print(C)
    C = C - 1
'''
'''
C = 2
while(C<=30):
    print(C,C**2)
    C = C + 2
'''
'''
x = input("What is your password:")
while(x != "UST"):
    print("Sorry wrong password")
    x = input("What is your password:")
'''   
''' 
x= int(input("Guess the number: "))
while(x != 50):
    if(x>50):
        print("too high")
    else:
        print("too low")
    x= int(input("Guess the number: "))
print("Congrats")
'''
'''
x = input("Enter a name: ")
while(x!= "stop"):
    x = input("Enter a name: ")
'''
'''
sum = 0
x = 1
n = int(input("Enter a positive integer: "))
while(x <=n):
    sum = sum + x
    x = x + 1
    print(sum)
'''
'''
x = int(input(" Enter a number or 0 to stop: "))
sum = 0
while(x != 0):
    sum = sum + x
    x = int(input(" Enter a number or 0 to stop: "))
print(sum)
'''
'''
x = int(input(" Enter a number or 0 to stop: "))
count_pos=0
count_neg=0
while(x != 0):
    if(x>0):
        count_pos = count_pos + 1
    else:
        count_neg = count_neg + 1 
    x = int(input(" Enter a number or 0 to stop: "))
print("Positive numbers:", count_pos)
print("Negative numbers:", count_neg)
'''
'''
i = int(input("Enter your grades:"))
sum = i
for i in range(1,6):
    i = int(input("Enter your grades:"))
    sum = sum + i
average = sum / 6
print("The average of your grades is:", average)
'''
'''
x = int(input(" Enter a number or 0 to stop: "))
max = 0
while(x != 0):
    if(x>max and x%2==0):
        max = x
    x = int(input(" Enter a number or 0 to stop: "))
print("The maximum even number is:", max)
'''
'''
n = int(input("Enter a positive integer: "))
sum = 1
for i in range(1,n+1):
    sum = sum * i
print("The factorial of", n, "is:", sum)
'''
'''
for i in range(1,11):
    print(i)
'''
'''
x = input("Enter a word: ")
for i in range(5):
    print(x)
'''
'''
for i in range(2,21,2):
    print(i)
'''
'''
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum = sum +i
print(sum)
'''
   
'''
count = 0
word = input("Enter a word: ")
for i in word:
    if (i =="a"):
        count = count + 1
        print(count)
'''
'''
for i in range(4):
    for j in range(4):
        print(i, end="")  
    print() 
'''
'''
for i in range(4):
    for j in range(4):
        print("*", end="")  
    print()
'''
'''
for i in range(7):
    for j in range(i):
        print(j ,end="")
    print()
'''
'''
for i in range(6):
    for j in range(i):
        print("*" ,end="")
    print()
'''   