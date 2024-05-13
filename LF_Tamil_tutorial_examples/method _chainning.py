#to do chainning use "return self" in the method,where we going to chainning the another method

class Users():
    def __init__(self,username,pwd):
        self.username=username               #instance variable
        self.pwd=pwd
        print("let's start",self.username)
    def register(self):
        print("registering",self.username)
        print(f"your pwd is {self.pwd},don't share to any one " )
        return self                                                 #must give,when try to perform method chainning
    def login(self):
        print("logging in",self.username)

user1=Users("Ram",12345)
user2=Users("Sam","afhh3515gg")
user1.register()
user2.register().login()             #method chainning