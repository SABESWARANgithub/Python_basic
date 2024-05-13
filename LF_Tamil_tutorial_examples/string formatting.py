name="Ram"
like1="apple"
like2="mango"
print(name+" likes "+like1+" and "+like2)

text="{} likes {} and {}"
print(text.format(name,like1,like2))

text="{0} likes {2} and {1}"
print(text.format(name,like1,like2))          #.format(0,1,2)

print("{} likes {} and {}".format(name,like2,like1))

print(f"the fruits liked by {name} are {like1} and {like2}")
'''
#also give by keywords
text1='{name} is {str(age)} years old '
print(text1.format(name="hari",age=12))
'''

#can add padding while formatting a string
#basically
print("***{msg}***".format(msg="hi"))

#for padding
print("***{msg:5}***".format(msg="hi"))
print("***{msg:<5}***".format(msg="hi"))             #totally it take 5 distance spaces & align the text to left
print("***{msg:>5}***".format(msg="hi"))              #totally it take 5 distance spaces & align the text to right
print("***{msg:^6}***".format(msg="hi"))          ##totally it take 6 distance spaces & align the text to center

#to format numbers
pi=3.14159
print("The val of pi is {}".format(pi))
print("The val of pi is {:.2f}".format(pi))

#by comma
sd=1000000000000000
print("the total amt is {:,}".format(sd))
'''
#to get the binary value for the given no    ??????-Doubt
v1=12
print("the binary val of {v1} is {:.b} ".format(v1))

    b-binary value,  o-octal value , x/X - hexa value , E - scientific notation value
'''

num = 'sabes'
print("The name is {num}".format(num=name))