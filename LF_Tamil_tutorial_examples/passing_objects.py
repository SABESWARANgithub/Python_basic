#to see,how to pass the object to one function

#Basic eg:
from  abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        color=None
        print("your are riding bike")
class Car(Vehicle):
    def start(self):
        color=None
        print("your are riding car")
b1=Bike()

b1.start()
c1=Car()
c1.start()

