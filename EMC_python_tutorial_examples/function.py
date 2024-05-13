#    """............""" - when use double triple quotes are called as "docstring"
#docstring is used to (documentaize the process of code)

def greet(name):
    print("hello",name)
name="ram"
greet(name)
greet("sam")


def sum_nn(num):
    result=num*(num+1)/2
    print(f"the sum of first {num} natural numbers is",result)
sum_nn(5)
sum_nn(3)
sum_nn(11)





# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# print(add(1,2))
# print(sub(2,1))

'''
ori_name="Ram"
ori_pass=str(123)
user_name=input("Enter your name:")
user_password=input("Enter your password:")
def validate(user_name,user_password):
    if(ori_name==user_name and ori_pass==user_password):
        print("Logging in")
    else:
        print("Enter corect details")
s=validate(user_name,user_password)
'''









