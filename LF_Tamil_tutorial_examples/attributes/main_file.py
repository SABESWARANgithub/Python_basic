
#to do some action/process,we need some data's;these data's are basically refered as "attributes"
#with that data's,we able to perform some process/action:these process/action is termed as "methods"   Eg:register,change pwd,login

#if we put these attributes & methods in a class;we can able to call/process for many times as we need, just by creating a object to a class
#eg:one website has many users,each user are refer to as each object

#in this file we going to give the necessary attribures(data's) & methods(func's,class,etc...)
class Users():
    def __init__(self,username,pwd):
        self.username=username               #instance variable
        self.pwd=pwd
        print("let's start",self.username)
    def register(self):
        print("registering",self.username)
        print(f"your pwd is {self.pwd},don't share to any one " )
    def login(self):
        print("logging in",self.username)

