#super keyword - use to access the constructor of its parent class
#Use the super keyword in the child class constructor

#basic eg:
# class Sample():
#     def __init__(self):
#         print("A")
#     def sam(self):
#         print("B")
# class Sem1(Sample):
#     def sem(self):
#         print("D")
# r=Sem1()


#using super keyword
'''
class Sample():
    def __init__(self):
        print("A")
    def sam(self):
        print("B")
class Sem1(Sample):
    def __init__(self):
        super().__init__()
        print("s")
    def sem(self):
        print("D")
s=Sem1()'''
'''
class Sample():
    def __init__(self):
        print("A")
    def sam(self):
        print("B")
class Sample1(Sample):
    def __init__(self):
        super().__init__()
        print("C")
    def sam1(self):
        print("D")
class Sample2(Sample1):
    def __init__(self):
        super().__init__()
        print("E")
    def sam2(self):
        print("F")
s=Sample2()'''





'''
class Sample():
    def __init__(self):
        print("A")
    def sam(self):
        print("B")
class Sample1():
    def __init__(self):
        super().__init__()
        print("C")
    def sam1(self):
        print("D")
class Sample2(Sample,Sample1):
    def __init__(self):
        super().__init__()
        print("E")
    def sam2(self):
        print("F")
s=Sample2()


print("Next:")
class Sample():
    def __init__(self):
        print("A")
    def sam(self):
        print("B")
class Sample1():
    def __init__(self):
        super().__init__()
        print("C")
    def sam1(self):
        print("D")
class Sample2(Sample1,Sample):
    def __init__(self):
        super().__init__()
        print("E")
    def sam2(self):
        print("F")
r=Sample2()
'''

# class Sad():
#     def __init__(self):
#         print("s")
# class Mad(Sad):
#     def __init__(self):
#         super().__init__()
#         print("m")
# m=Mad()

#when we use super keyword,must inherit the another class;otherwise the super keyword is not use/effective


class User():
    def __init__(self,username,pwd):
        self.username=username
        self.pwd=pwd
        print("the User:",self.username)
    def greet(self):
        print("User:",self.username)
class Teacher(User):
    def __init__(self,username,pwd,profession,subject):
        super().__init__(username,pwd)
        self.profession=profession
        self.subject=subject
        print("Teacher",self.username)
    def greet(self):
        print("let's take class")
class Student(User):
    def __init__(self,username,pwd,dept,section):
        super().__init__(username,pwd)
        self.dept=dept
        self.section=section
        super().greet()
    def greet(self):
        print("name:",self.username)
        print("pwd:",self.pwd)
        print("dept:",self.dept)

# teacher=User("ram",123)
# teacher1=Teacher("teaching","maths")
# teacher1.greet()
student1=Student("faf",64658,"cse","d")
student1.greet()




