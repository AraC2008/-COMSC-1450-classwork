'''
x = float(input("What is your GPA? "))
y = int(input("What is your SAT score? "))
if(x>=3.5 and x>=1000):
    print("Accepted")
elif(x>=3.0 and y>=1100):
    print("Accepted")
elif(x>4.0 and x<0.0):
     print("Invalid GPA")
elif(y<0):
    print("Invalid SAT score")
elif(x<3.5 and y<1000):
    print("Rejected")
'''
'''
w = int(input("what is the weight of the package in kg?: "))
x = input("Are you a premium member? (yes/no): ")
if( x == "yes"  and w>=5):
    print("Free Shipping")
elif(w<=2):
    print("$5")
elif(w>2 and w<=5):
    print("$10")
elif(w>5 and w<=10):
    print("$15")
elif(w>10):
    print("$25")    
elif(w==0 and w<0):
    print("Invalid weight")
'''
'''
Order_amount = float(input("What is the order amount?: "))
Delivery_distance = float(input("What is the delivery distance in km?: "))
if(Order_amount>=50):
    print("Free delivery")
elif(Order_amount>=30 and Order_amount<=49.99 and Delivery_distance<=5):
    print("$3 delivery")
elif(Order_amount<30 and Delivery_distance<=5):
    print("$5 delivery")
elif(Delivery_distance>5):
    print("Additional $2 delivery")
'''
'''
sum = 0
count = 0
while(count<5):
    sum = sum + count
    count = count + 1
print(sum)
'''