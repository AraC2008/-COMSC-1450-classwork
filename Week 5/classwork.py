
'''
total_sum = 0
for i in range(1,51):
    if i % 3 == 0:
        total_sum +=i
print(total_sum)
'''
'''
Age = int(input("Enter your age: "))
if Age < 0:
    print("invalid Age")
else:
    if Age < 13:
        price = 5
    else:
        if Age <= 17:
            price = 8
        else:
            price = 12
    print("Ticket Price: $", price)
    '''
'''
Total_sum = 0
for num in range(1,51):    
    if num % 3 == 0 and num % 5 == 0:
        Total_sum = Total_sum + num
print(Total_sum) 
'''
'''
def factorial(n):
    count=1
    for i in range (1,n+1):
        count = count * i
    return count
print(factorial(5))
'''
'''
def countdown (n):
     if n == 0:
         return
     print(n)
     countdown(n-1)
countdown(5)  
'''