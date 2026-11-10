'''
x=[3,6,9,12,15]
for i in x:
    print(i)
'''
'''
x =[3,6,9,12,15]
print(x[0])
print(x[-1])
'''
'''
x =[10,20,20,30,40,5,4,3,2,1]
search_element = int(input("Enter an element to search: "))
if search_element in x:
    print (search_element," is in the list")
else:
    print(search_element, "isnt in the list")

'''



'''
x =[3,6,9,12,15]
total =0
for i in x:
    total = total + i
print(total)
'''
'''
x =[3,6,9,12,15]
total =0
for i in x:
    total = total + i
    average = total / len(x)
print(average)
'''
'''
x=[3,6,9,12,15]
max =x[0]
for i in x:
    if max < i:
        max = i
print(max)
'''
'''
x=[3,6,9,12,15]
min =x[0]
for i in x:
    if min > i:
        min = i
print(min)
'''
'''
x = [2,3,4,5,6,7,8,6,4]
even = 0
odd = 0
for i in x:
    if i %2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(even,"is how many are even.", odd, " is how many are odd")
'''
'''
x = [1,2,3,4,5,6,7,7,8,8,9,9]
special_num = []
for i in x:
    if i not in special_num:
        special_num.append(i)

print(special_num," is the list without duplicates")
'''
'''
x = [-2,3,4,-6,-7,5,8]
pos = []
neg = []
for i in x:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
print(pos, "is the list thats positive", neg, "is the list thats negative")
'''
'''
words = ["apple","pen","dog","bannana","orange"]
long_words = []
for i in words:
    if len(i)> 4:
        long_words.append(i)
print(long_words)
'''
'''
x =[2,3,4,5]
squares = [i**2 for i in x]
print(squares)
'''
'''

x=(3,6,9,12,15)
y=list(x)
print(y)
y.append(18)
x =tuple(y)
print(x) 
'''

'''
x=(3,6,9,12,15)
y=list(x)
print(y)
y.remove(9)
x =tuple(y)
print(x)   
'''
'''
x=(3,6,9,12,15)
for i in x:
    if 20 in x:
        print("20 is present in the tuple")
    else:
        print("20 is not present in the tuple")
'''