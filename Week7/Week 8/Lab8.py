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
x=[3,6,9,12,15]
max =x[0]
for i in x:
    if max < i:
        max = i
print(max)