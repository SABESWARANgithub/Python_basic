#class name can be caps(or)small
# class vehicle():
#     def __init__(self):
#         print("jh")
# s=vehicle()

# class Students:
#     def __init__(self):
#         print("hi")
#     def sam(self):
#         print("hello")
# s=Students()
# defs.sam()

'''
class Laptops:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def details(self):
        print(self.brand)
        print(self.price)
sam=Laptops("HP",20000)
ram=Laptops("asus",25000)
sam.details()
ram.details()
'''

class Teacher:
    def __init__(self,name,reg_no):
        self.name=name
        self.reg_no=reg_no
    def display(self):
        print("Name:",self.name)
        print("Reg.no:",self.reg_no)
t1=Teacher("ram",123)
t2=Teacher("Sam",345)
t1.display()
t2.display()





