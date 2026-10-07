'''
def countdown (n):
     if n == 0:
         print("liftoff")
         return
     print(n)
     countdown(n-1)
countdown(5)
'''
'''
def countdown(n):
    if n<=0:
        print("liftoff!")
    else:
        print(n)
        countdown(n-1)
countdown(5)      
'''
'''
def print_range(start,end):
    if start > end:
        return
    print(start)
    print_range(start +1,end)
print_range(3,8)
'''
'''
def sum (n):
    if n == 0:
        return n
    return n+ sum(n-1)
sum(5)
'''
'''
def count_down_evens (n):
   if n < 0:
      print("Done!")
   else: 
     print (n)
     count_down_evens(n-2)
count_down_evens(8)
'''
'''
def power_of_two (n):
    if n == 0:
        return 1
    else:

        return 2 * power_of_two (n-1)
print(power_of_two(4))
'''
'''
Larger = lambda (x,y): x if x>y else y 
print(Larger(8,12))
'''
'''
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(7))
'''
'''
Pos_neg = lambda x: "Negative" if x < 0 else "positive"
print(Pos_neg(-5))
'''
'''
Add = lambda x,y: x+y
print(Add(4,10))
Area = lambda r: 3.14159*r**2
print(Area(4))
'''
