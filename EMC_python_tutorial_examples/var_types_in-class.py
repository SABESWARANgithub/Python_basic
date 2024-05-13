#types of variables in class - instance variable & class variable
'''
class Phones():
    price=10000                       #class variable
    def __init__(self,brand):
        self.brand=brand              #instance variable
    def details(self):
        print("price:",self.price)
        print("brand:",self.brand)
    price=20000                       #updated - class variable
samsung=Phones("samsung")
nokia=Phones("nokia")
samsung.details()
nokia.details()
'''

class User:
    users=0                                  #class variable
    def __init__(self,username,pwd):
        self.username=username               #instance variable
        self.pwd=pwd                         #instance variable
        print("let begin",self.username)
        User.users+=1
    def reg(self):
        print("registering",self.username)
        print("your pwd,",self.pwd)
    def log(self):
        print("login in",self.username)
sam=User("Sam",235)
ram=User("Ram",174)
ravi=User("Ravi",6768)
sam.reg()
ram.reg()
ravi.reg()
ravi.log()
print(User.users)