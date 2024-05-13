'''
acces the parent class by its child class(when one class access the functions & variables of another class)
types - single inheritance,multi-level inheritance,multiple inheritance,
        hierarchial inheritance,hybrid inheritance

'''

#single inheritance - to access one class to another class
'''
class Dad():
    def phone(self):
        print("Phone")
class Mom():
    def amt(self):
        print("my amt")
class Son(Dad,Mom):
    def laptop(self):
        print("laptop")
ram=Son()
ram.laptop()
ram.phone()
ram.amt()
'''

#muti-level inheritance - to access two classes from one class
'''
class Dad():
    def phone(self):
        print("Phone")
class Mom(Dad):
    def amt(self):
        print("my amt")
class Son(Mom):
    def laptop(self):
        print("laptop")
ram=Son()
ram.amt()
ram.phone()
'''

#hierarchical inheritance - Eg: 3 child classes accessing 1 parent class
class Mom():
    def money(self):
        print("my money")
class Son1(Mom):
    def son1(self):
        print("Moms-1 money")
class Son2(Mom):
    def son2(self):
        print("Moms-2 money")
class Son3(Mom):
    def son3(self):
        print("Moms-3 money")
son1=Son1()
son2=Son2()
son3=Son3()
son1.son1()
son1.money()
son2.son2()
son2.money()
son3.son3()
son3.money()


#multiple inheritance - avoid mostly - Connections based on diamond shaped between classes

#Hybrid inheritance - accessing in all format of inheritance types declared before
'''
class Grand_Father():
    def grandf(self):
        print("1st")
class Grand_mother(Grand_Father):
    def grandm(self):
        print("2nd")
class Father(Grand_mother):
    def father(self):
        print("3rd")
class Son_1(Father):
    def son_1(self):
        print("4th")
class Son_2(Father):
    def son_2(self):
        print("5th")
class Son_3(Father):
    def son_3(self):
        print("6th")
ram=Father()
ram.grandf()
ram.grandm()
sam=Son_3()
sam.grandf()
sam.grandm()
sam.son_3()
'''
#Before eg. using with pass keyword  / pass - is use to access the function of its parent class
class Grand_Father():
    def grandf(self):
        print("1st")
class Grand_mother(Grand_Father):
    def grandm(self):
        print("2nd")
class Father(Grand_mother):
    pass
class Son_1(Father):
    pass
class Son_2(Father):
    pass
class Son_3(Father):
    pass
ram=Father()
ram.grandf()
ram.grandm()

sam=Son_3()
sam.grandf()
sam.grandm()
