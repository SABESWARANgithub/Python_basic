# try:
a=("The king was going to defeat the army by his own")
print(a.count("a"))
print(a.replace("a","z",))
print(a.find("t",10))
print(a.isalpha())                    #shows false because there is gap b^n each word
print(a.isalnum())
print(a.__add__("\nthe king was also a demon"))
print(len(a))
# print(slice(5,20,2))
print(a)
print(a.find("z"))                    #if the value is not there it give negetive values as output
b="123"
print(b.isalnum())
print(b.isalpha())
print(b.isdigit())
print(b.isdecimal())
print(a.title())
print(a.capitalize())
print(a)
print(a.islower())
c=a.title()
print(c.istitle())
print(a)
print(c)
# except AttributeError as e:
#     print("Some error had occured",e)