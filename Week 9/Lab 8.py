'''
d = {'Apples': 50, 'Bananas': 30, 'Oranges': 25}
d.update({'Bananas': 45})
d.update({'Mangos': 15})
d.pop('Oranges')
print(d)
'''
'''
d = {'Apples': 50, 'Bananas': 30, 'Oranges': 25}
def get_stock(inventory, item):
    return inventory.get(item,"Not in stock")

print(get_stock(d, 'grapes'))
'''
'''
keys = ["Name", "Age", "Role"]
values = ["Alex", 24, "developer"]
d = dict(zip(keys, values))
print(d)
'''
'''
d = {"Alex": 55, "John": 30, "Sarah": 57}
for key, value in d.items():
    if value > 50:
        print(f"{key} is over 50 years old.")
'''
'''
d = {'A': 50, 'B': 30, 'C': 25}
d2={}
for key, value in d.items():
    d2[value] = key
    print(d2)
print(d)
'''
'''
default_settings ={'theme': 'light', 'font_size': 12, 'show_tips': True}
user_settings = {'theme': 'dark', 'font_size': 14}
default_settings.update(user_settings)
print(default_settings)
'''
'''
x = {1, 2, 3, 4, 5}
set.add(6)
print(set)
'''
'''
x = {1, 2, 3, 4, 5}
x.remove(3)
print(x)
'''
set = {1, 2, 3, 4, 5}
set1 = {4, 5, 6, 7, 8}
print(set & set1)