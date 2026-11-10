'''
class book:
    def __init__(self,Title,Author,Price):
        self.title = Title
        self.author = Author
        self.price = Price
    def apply_discount(self,percentage):
        self.price = self.price - (self.price * percentage/100)
        
    def get_details(self):
        print("Title:", self.title, "Author:",self.author,"Price:" , self.price)
   




b1 = book("The rainbow fish", "Katie Shepard" , 27.75)
b2 = book("Harry Potter", "J.K. Rowling", 35.46)
b3 = book("A series of unfortunate events", "Holly" , 37.57)
b1.apply_discount(10)
b1.get_details()
b2.get_details()
'''
'''
class Rectangle:
    def __init__(self,Len,Wid):
        self.length = Len
        self.width =Wid
    def area(self):
        print("area:", self.length*self.width)
    def perimeter(self):
        print(self.length+self.lenth+self.width+self.width)
    def display(self):
        print(f"Length:,{self.length} , Width: , {self.width}")
R1 = Rectangle(5,10)

print("Area: ", R1.area, "Perimeter: ", R1.perimeter)
R1.display()
'''
'''
class pet:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        self.hunger = 50
    def feed(self):
        self.hunger -= 15
    def get_status(self):
        print(f"{self.name} the {self.species} has the hunger level of {self.hunger}.")

pet1= pet("Luna", "Cat")
pet2 = pet("Buddy", "Dog")
 

pet1.feed()
pet2.feed
pet2.feed

pet1.get_status()
pet2.get_status()
'''
'''
class car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0
    def drive(self, miles):
        self.odometer += miles
    def get_status(self):
        return f"A {self.make} {self.model} with {self.odometer} miles."

C1 = car("Chevorlet", "Impala")
C1.drive(150)
C1.drive(85)
print(C1.get_status())
'''
'''
class Student:
    def __init__(self,n):
        self.name = n
        self.grades = []
    def add_grade(self,score):
        self.grades.append(score)
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades)/ len(self.grades)

s1 = Student("Dave")
s1.add_grade(71)
s1.add_grade(81)
s1.add_grade(77)

print("Student: ", s1.name, "Average Grade: ", s1.get_average())
'''
'''
class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, price):
        self.items[item_name] = price
    def get_total(self):
        return sum(self.items.values())
    
cart = ShoppingCart()
cart.add_item("Eggs" , 15.25)
cart.add_item("Cheese", 17.35)
print("Total cost: ", cart.get_total())
'''
'''
class BankAccount:
    def __init__(self,account_holder,balance):
        self.__account_holder = account_holder
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount is positive!")
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

b1 = BankAccount("Laura adams", 560)
b1.get_balance()
b1.deposit(60)
b1.withdraw(50)
'''