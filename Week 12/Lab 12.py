'''
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
            return f"{self.name} is eating."
class Cat(Animal):
     def meow(self):
         return f"{self.name} says Meow!"
my_cat = Cat("Whiskers")
print(my_cat.name)
print(my_cat.eat())
print(my_cat.meow())
'''
'''
class Shape:
    def describe(self):
        print("This is a generic shape.")
class Square(Shape):
    def describe(self):
        print("This is a square with four equal sides.")
my_square = Square()
my_square.describe()
s2 = Shape()
s2.describe()
'''
'''
class Rectangle:
    def __init__(self,Len,Wid):
        self.length = Len
        self.width = Wid
    def area(self):
        return self.length * self.width
class CubeBase(Rectangle):
    def perimeter(self):
        return 2 * (self.length + self.width)

R2 = CubeBase(5, 10)
print("Area of rectangle:", R2.area())
print("Perimeter of cube base:", R2.perimeter())
'''

'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        return f"Manager Name: {self.name}, Salary: {self.salary}, Department: {self.department}"
manager1 = Manager("Alice", 80000, "HR")
print(manager1.display())
employee1 = Employee("Bob", 50000)
print(employee1.display())
'''
'''
class vehicle:
    def __init__(self, brand,fuel_level):
        self.brand = brand
        self.fuel_level = fuel_level
    def drive(self, miles):
        self.fuel_level -= miles * 0.5
        print(f"{self.brand} drove {miles} miles. Fuel level is now {self.fuel_level}.")
class electric_vehicle(vehicle):
    def __init__(self, brand, fuel_level, battery_health):
        super().__init__(brand, fuel_level)
        self.battery_health = 100
    def drive(self, miles):
        print("Silent electric drive..")
        super().drive(miles)
ev1 = electric_vehicle("Tesla", 100, 100)
ev1.drive(20)
'''
'''
class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def final_price(self):
        return self.price
class Electronical_product(product):
    def __init__(self, name, price, warranty_Cost):
         super().__init__(name, price)
         self.warranty_Cost = warranty_Cost
    def final_price(self):
        return self.price + self.warranty_Cost
class clearenceElecronic(Electronical_product):
    def __init__(self, name, price, warranty_Cost, discount_percent):
        super().__init__(name, price, warranty_Cost)
        self.discount = discount_percent
    def final_price(self):
        total = super().final_price()
        discount_amount = total * (self.discount / 100)
        return total - discount_amount
laptop = clearenceElecronic("Laptop", 1000, 100, 10)
print("Final price of the laptop:", laptop.final_price())
phone = Electronical_product("Phone", 800, 50)
print("Final price of the phone:", phone.final_price())
apple = product("Apple", 5)
print("Final price of the apple:", apple.final_price())
'''