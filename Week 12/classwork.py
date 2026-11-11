'''


class Student:
    def __init__(self,n,a,gp):
        self.name = n
        self.age = a
        self.gpa = float(gp)
    def display(self):
        print("This is the student info:",self.name,self.age,self.gpa)
    def calculate_gpa(self):
        return self.gpa * 2
        
s1 =Student("Sara", 18,3.5)


s2 = Student("Dave", 19,3.8)

s3 = Student("John",21,2.9)
s1.name = "Lara"
s1.display()
s2.display()
print(s1.calculate_gpa())


'''



'''
class Person:
    def __init__(self,n,a,Address):
        self.name = n
        self.age = a
        self.address = Address
    def display(self):
        print(self.name,self.age,self.address)
class Student(Person):
    def __init__(self,n,a,Address,gpa):
        super().__init__(n,a,Address)
        self.gpa = gpa
    def display(self):
        super().display()
        print("GPA:",self.gpa)
class Employee(Person):
    def __init__(self,n,a,Address,salary):
        super().__init__(n,a,Address)
        self.salary = salary
    def display(self):
        super().display()
        print("Salary:",self.salary)
class TA(Person):
    pass

s1 = Student("Sara", 18,"123 Main St", 3.5)
e1 = Employee("Dave", 19,"456 Oak St", 5000)
ta1 = TA("John",21,"789 Pine St")


s1.display()
e1.display()
'''