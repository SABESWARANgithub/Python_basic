#refer notes also
a=1
b=2
c=1
print(id(a))
print(id(b))
print(id(c))
print(id(a)==id(b))
print(id(a)==id(c))
print("\n")
c=c+1
print(id(c))
print(id(b)==id(c))
print(id(a))
a="Ram"
print(id(a))

#Refer how data is allocated; in notes
class Box:
    def __init__(self,l):
        self.len=l             #instant variable

b=Box(10)
print(b.len)

#how memory allocate in/with functions

def xv(x):
    x=10

x=14
xv(x)


# int,float,string,tuple - immutable

#list,set,....- mutable

