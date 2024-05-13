#Bitwise operators : &-and , |-or , ~-not , ^-exor , >>-right shift , <<-left shift

# mini calculator

# a=int(input("Enter !st num:"))
# b=int(input("Enter 2nd num:"))
# operation=input("add/sub/mul/div =")
# if (operation=="add"):
#     print(a+b)
# elif(operation=="sub"):
#     print(a-b)
# elif(operation=="mul"):
#     print(a*b)
# elif(operation=="div"):
#     print(a/b)
# else:
#     print("invalid option")

'''
a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print("Your choices:1.add/2.sub")
choice=input("Enter your choice:")
if(choice=="1"):
    print(add(a,b))
elif(choice=="2"):
    print(sub(a,b))
else:
    print("invalid choice")
'''


salary= int(input("Your salary for a whole year:"))
age= int(input("your age:"))
if (salary<=200000 and age>=18):
    name=input("enter your name:")
    loan_amt=int(input(("Enter required loan amt:")))
    if (loan_amt<=300000):
        print(name,f"you are eligible for {loan_amt} loan amount")
    else:
        print("the loan amount should be not more than 3lakhs")
else:
    print("you are not eligible")

