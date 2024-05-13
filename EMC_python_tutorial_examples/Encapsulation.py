'''
one of the important ..oops.. concept

Access modifiers -   i)public variable-(no _)-can be access by/at any class
                    ii)protected variable-(single _)-can be access by inherited classes
                   iii)private variable-(double __)-can be access within the class/use when we don't like to change/update the declared variable in the  classs
                                           Eg:def __init__(self):
                                                  self.__name=name      #private variable
'''
#  Basic-Eg:
# class sample():
#     def __init__(self,name):
#         self.name=name
#     def sam(self):
#         print(self.name)
# s=sample("Ram")
# s.sam()

# class Sample():
#     def __init__(self):
#         self.name="Ram"
# s=Sample()
# print(s.name)
# s.name="Sam"               #when we don,t like to update the value by anyone; use private variable method
# print(s.name)

'''
class Sample():
    def __init__(self):
        self.__name="Ram"
    def sam(self):
        print(self.__name)
s=Sample()
s.sam()              #after updating the name & then calling it; it shows orinigal value only,not show the updated value:the private variable are not like to update it
s.name="Sam"
s.sam() '''

#Eg - protected variable
'''
class Sample():
    def __init__(self):
        self._name="Ram"        #protected variable
    def sam(self):
        print(self._name)
class Sample1(Sample):
    pass
s=Sample()
s.sam()
s1=Sample1()
s1._name="Sam"
s1.sam()
'''

#with the use of these public/protected/private variables,able to achieve encapsulation

#Encapsulation: combining all the attributes and the methods that the class needs under one umbrella (class itself) makes your code easy to maintain.
#Abstraction: hiding away the implementation details from the external user which makes your code easy to be shared with other developers