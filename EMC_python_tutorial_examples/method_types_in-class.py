#types of methods in class - instance method,class methhod & static method
#functions are also called as methods
#where_ever,we put self to creating functions are called instance method

#class method - two ways-by using decorators(Mostly not use) & pass the parameter/argument as "cls"
'''
class Laptop:
    chargerType="C-type"
    def __init__(self):
        self.brand=" "
        self.price=" "
    def setDetails(self,brand,price):
        self.brand=brand
        self.price=price
    def getDetails(self):
        print("brand:",self.brand)
        print("Price:",self.price)

    def changeChargerType(cls):         #passing cls parameter
        cls.chargerType="B-type"
        print("charger type changed to",cls.chargerType)
hp=Laptop()
hp.setDetails("HP",10000)
hp.getDetails()
Laptop.changeChargerType(Laptop)
'''

#static method - by using decorators
class Laptop:
    chargerType = "C-type"
    def __init__(self):
        self.brand = " "
        self.price = " "
    def setDetails(self, brand, price):
        self.brand = brand
        self.price = price
    def getDetails(self):
        print("brand:", self.brand)
        print("Price:", self.price)
    def changeChargerType(cls):  # passing cls parameter
        cls.chargerType = "B-type"
        print("charger type changed to", cls.chargerType)
    @staticmethod
    def info():
        print("this is static")
hp = Laptop()
hp.setDetails("HP", 10000)
hp.getDetails()
Laptop.changeChargerType(Laptop)
hp.info()