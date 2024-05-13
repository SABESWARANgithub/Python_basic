#global variable , local variable

#local variable -mmore(1st) preference than global variable

num=8                  #num - global variable
def wel(name):         #name - local variable
    num=12             #num - local variable
    print("Welcome",name)
    print(num)
wel("Ram")
print("the num is",num)
while num<100:
    print(num,end=",")
    num+=10


#to declare the local variable as global variable
num=8
def welc(name):
    global num             #by giving like this,the local variable is changed into global variable
    num=12
    print("\nWelcome",name)
    print(num)
welc("Ram")
print("the num is",num)
while num<100:
    print(num,end=",")
    num+=10


