'''#basic eg's:
def tot(n1,n2):
    return n1+n2
print(tot(2,3))

def total(n1,n2):
    return n1+n2
print(total(2,3,4))              #it only have 2 parameters to pass,but we pass 3 parameters
'''

#but when like to pass more parameters,even the function have limited parameters to pass
#Use variable length arguments:
def total1(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(total1(1,2,3,4,5))


#we can give the length arguments (args) also as keyword arguments (kwargs) , to use in the way of dictionary
#kwargs - packs all the keyword arguments into a dictionary

def address(**kwargs):
    for key,val in kwargs.items():
        print(key)
        print(val)
    for key in kwargs.keys():
        print(key)
address(door_no=24,area="nadu nagar",ward="south",city="hthgjgj")


#Default arguments - by givng the default value in the last argument is best option

# def samp(a,b,c=3):
#     return a+b+c
# print(samp(1,2))
# print(samp(1,2,4))


#passing list
def print_list(list):
    for i in list:
        print(i.title(),end=",")
names=["RAM","SAM","RAVI","GOPI"]
print_list(names)
print("\n")
print(names)

#this example changes the original list itself
def printlist(list):
    for i in range(0,len(list)):
        list[i]=list[i].title()
        print(list[i],end=",")
names=["faf","Koli","kaali","Rast"]                  #original list(declared as in the way of global variable)
printlist(names)
print("\n")
print(names)                           #the original list itself updated by .....

#we just declare to update the list within the function only but the original itself had updated
#when we don't like update the orinal list use [:]

def printlist(list):
    for i in range(0,len(list)):
        list[i]=list[i].title()
        print(list[i],end=",")
names=["faf","Koli","kaali","Rast"]
printlist(names[:])
print("\n")
print(names)


