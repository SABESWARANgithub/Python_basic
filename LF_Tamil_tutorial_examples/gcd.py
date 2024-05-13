#Multiple assignment
'''
a,b,c=1,2,3
print(c)

like=dislike=100
print(like)
print(dislike)
'''

'''
import math
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
gcd_result=math.gcd(a,b)
print("the gcd of "+str(a)+" and "+str(b)+" is",gcd_result)
'''



import math
a=input("Enter the 1st number:")
b=input("Enter the 2nd number:")
gcd_result=math.gcd(a,b)
print(f'the gcd of {a} and {b} is {gcd_result}'.format(a,b,gcd_result))


