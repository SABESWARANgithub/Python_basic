import math
'''
a=1.2
print(math.ceil(a))          #roundOff to upcoming/next absolute value
print(math.floor(a))         #roundOff to before absolute value
b=4
c=16
d=-1
print(range(c))
print(range(b))
print(round(a))          #roundOff
print(abs(d))            #absolute
print(min(a,b))            #which is minimum among a & b
print(max(a,b,c,d))          ##which is maximum among a,b,c,d
print(math.factorial(b))
print(math.gcd(b,c))
print(math.factorial(3))
print(math.factorial(c))
print(a**3)
print(math.pow(c,2))
print(math.comb(7,5))           #print total no.of possible combinations
print(math.comb(b,c))            #not use float type data,while using "comb" method in math operations
print(math.comb(c,b))

'''
         #Input handling
         
height=int(input("What is your height:"))
height_inches=height/2.54
print("you are "+ str(height_inches) +" inches tall")
heightInches="{:.2f}".format(height/2.54)
print("you are "+ heightInches +" inches tall")