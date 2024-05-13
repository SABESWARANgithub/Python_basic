'''
method overriding - update/change the method/function,which was already declared
                  to override the method/func in the child class ,which is already declared in the parent class
polymorphism - when we like/use to override the function which was already declared
derived class - when one class inherits from another class that class is called...
'''

# class Animal():
#     def sound(self):
#         print("A")
# class Dog(Animal):          # Derived class
#     def sound(self):
#         print("B")
# s=Dog()
# s.sound()

class Animal():
    def __init__(self):
        print("A")
    def sound(self):
        print("B")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("C")
    def sound(self):
        print("D")
s=Dog()
s.sound()

#Eg's for class & object & inheritance & polymorphism
# class Person():
#     def __init__(self,name):
#         self.name=name
'''class Student():
    def __init__(self,name,grade):
        self.name=name
        self.grage=grade
    def disply(self):
        print(self.name,self.grage)
# p=Person("Ram")
s=Student("ram","A+")
s.disply()
'''

#task-1  - polymorphism & overridding
'''class Vehicle():
    def start(self):
        print("vehicle stared")
class Car(Vehicle):
    def start(self):
        print("car stared")
c=Car()
c.start()'''

#task-2  ????Doubt -refer
class Employee():
    def __init__(self,name,salary):
        self.name=name                           #called as initializing
        self.salary=salary
class Manager():
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("salary:",self.salary)
        print("Dept:",self.department)
ma=Manager("ram",20000,"Maintaining")
ma.display()
