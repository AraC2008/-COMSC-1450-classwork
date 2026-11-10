'''
x=[]
total = 0
for i in range (5):
    n = int(input("Enter a number: "))
    x.append(n)
    total = total + n
print(total)
'''
'''
def sum(*x):
    total = 0
    for i in x:
        total = total + i
    return total
print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4,5))
'''
'''
d ={'Name':'Sarah','Age':27,'score':98}
print(d['Age'])
print(d['Name'])
d['Name'] ='Dave'
print(d['Name'])
d['Score']=9
print(d['Score'])
d['Program'] = 'Python'
print(d)
print(d.get('School','Not Found'))
print('*****')
d.update({"Age": 30})
print(d)
d.update({"State": 'TX'})
print(d)
print(len(d))
d.pop('Score')
print(d)
d.popitem()
print(d)
del(d['Score'])
'''
'''
d ={'Name':'Sarah','Age':27,'score':98}
print(d)
for i in d:
    print(d[i])
for i in d.keys():
    print(i)    
    for i in d.values():
        print(i)
        for i, j in d.items():
            print(i, j)
'''
'''
names = ['Sarah','Dave','John']
ages = [27, 30, 25]
d = dict(zip(names, ages))
print(d)
'''