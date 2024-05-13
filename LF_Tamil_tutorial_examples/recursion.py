#when we like to call the func again & again from the func itself is called recursion

#basic eg

def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print(fact(3))

import math
s=fact(3)
print(s)

#fibonanci series
n=int(input("Enter no:"))
num1=0
num2=1
next_num=num2
count=0
while count<=n:
    print(next_num,end=" ")
    count+=1
    num1,num2=num2,next_num
    next_num=num1+num2
print()

'''
#fibonanci series in simplest method
n1=0
n2=1
count=0
while count<n:
    print(n1,end=" ")
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
'''

#returning dictionaries
#normall we use to return a single value at a time,but when to return many/multiple values put them in dictionary and return it
def user_info():
    user={"name":"ram","age":23,"city":"chennai","state":"tamilnadu"}
    return user
user=user_info()
print(user)
