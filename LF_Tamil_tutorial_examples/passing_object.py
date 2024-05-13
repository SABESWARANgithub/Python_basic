'''
going to see,how to pass the object to function  &  what is "duck typing"
duck typing - importance to methods more than objects;
   why this name comes -
       proverb - "it's looks like a duck & quacks like a duck;then it"s a duck" ;
                        like this the attributes in that class & that methods are only important ; the object is more important
              if that class & methods are right it shows output, not bouther the object because python
                                 is "dynamically typed language" ; in java,c++ its not possible
'''
class Vehicle:
    def start(self):
        pass
    def stop(self):
        pass
class Bike(Vehicle):
    color=None
    def start(self):
        print("your are riding bike...")
    def stop(self):
        print("stop ridding bike...")
class Car(Vehicle):
    color=None
    def start(self):
        print("your are riding car....")
    def stop(self):
        print("stop riding car...")
def set_color(car,color):
    car.color=color

c=Car()
b=Bike()
set_color(c,"blue")        #here we passing the object for Car class & color
set_color(b,"black")      #here we passing the object for bike class & color,it's shows correct output; even if we given the set_color method parameters as (car,color)
                                           #by assing the bike object to the car parameter,it re-assign (override) it & shows the correct output
print(c.color)
print(b.color)

'''
eg for some reference
all are basically refered in the way of object
'''

num = 10           #the 10 is known as integer object
list1=[1,2,3]      #the [1,2,3] its a type of list object
'''

#before eg: with extra information
class Vehicle:
    def start(self):
        pass
    def stop(self):
        pass
class Bike(Vehicle):
    color=None
    def start(self):
        print("your are riding bike...")
    def stop(self):
        print("stop ridding bike...")
class Car(Vehicle):
    color=None
    def start(self):
        print("your are riding car....")
    def stop(self):
        print("stop riding car...")
def set_color(obj,color):    #we no need to give the parameter as car only as before eg,give any name
    obj.color=color
    obj.start()      # this way of calling method is known as "duck typing"
    obj.stop()        #duck typing - immportance to methods , more than objects

c=Car()
b=Bike()
set_color(c,"blue")
set_color(b,"black")

print(c.color)
print(b.color)
'''