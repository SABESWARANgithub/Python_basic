'''
abstract defines as,it just an imagination,not have any definite structure,.... Eg:abstract idea,etc...

 Abstarct class    -   give all the common methods in a "Vehicle" class;by giving like this is called the "Abstract class"
 Concreate class    -   the class,which are remaining from the abstract class are called as "concrete class"
'''

'''
#eg:
class Vehicle:
    def start(self):
        pass
    def stop(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("your are riding bike...")
class Car(Vehicle):
    def start(self):
        print("your are riding car....")
truck=Vehicle()
truck.start()            #no output will show,because we just give pass
audi=Car()
audi.start()
audi.stop()              #it inherits the stop func/method from its parent(abstract) class; no output will show,because we just give pass
'''

#basically not allow to create object for common class/abstract class

'''
-  why use OOP concept,to just keep these classes as blueprint & create the realtime objects as many we need,these are just known as real time entity
In java,c++;  we just create the abstract class by mentioning keyword   Eg:abstract class vehicle
----  but in python;use ABC module

      from abc import ABC,abstractmethod
      class Vehicle (ABC):                   #abstract class
      
          @abstart method                    #decorator to mention the methods as,these are methods which are under abstract class
          def start(self):                   #abstract method 
              pass                           #like this we can give many abstract methods as we need
              
by using this method,not able to create object for abstract class;create the object only for the child(or).... classes
 -  what was the use of this abstract(vehicle)class ,to give the common methods for the  classes in this vehicle(abstract) class
 to give these as like methods  to,implement/use these methods from the abstract class(vehicle class)
 
 
 why we use this way to create abstract class, to protect to not to create object for the abstract class
    only able/force  to create the object for the child classes,which are inherited from the abstract class
Eg:
class Vehicle:
    @abstractmethod
    def start(self):
        pass
class Bike(Vehicle):            need to implement/define all the methods from the abtract class,not use pass
     pass                    if not,it shows error;when we try to create the object for that child class,when the class is not implement/override the methods which has already declared in the abstract class
'''

from abc import ABC, abstractmethod, abstractclassmethod


@abstractclassmethod
class Vehicle(ABC):
    def start(self):
        print("Riding")


class Bike(Vehicle):
    def start(self):
        print("your are riding bike")

    def stop(self):
        print("stop ridding the bike...")


b = Bike()
b.start()
b.stop()

#not able to create object for the abstract class
#the classes inheriting from abstract class must override all the abstract methods
