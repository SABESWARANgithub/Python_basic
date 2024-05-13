'''
- Lambda is usually known as anonymous function ; because when we like to use one func for a one time ;
                                                 & there is no use in it after that ; these type of using a func for a time ;
                                                                                                          is called as anonymous func
Eg:
def sad(..):
      print(....)         #this type of func can reuse many times we need

s=lambda x:x+10          output: 12
print(s(2))              this type of func can also able to re-use many times ;
                                       but this lambda func intension/purpose  -  for framed/developed this lambda func is not that

-- by using lambda keyword ;can use lambda func
-- don't able to write the large func as/in lamba ; only able to code in lambda format
                                                   when we going to declare/complete only one expression ;
                                                                       we can define it by using lambda
by using lambda we can get many parameters as we need ; Eg: lambda x,s,t,u,.....n:exp
                                                                    (parameters) : expressions/operation (what we going to conclude)
                                           able to give many parameters as need  :  but only able give only one expression
'''

'''
#basic eg:
def add(x):
    return x+10
print(add(2))

#we can short this code using lambda
add=lambda x:x+10
print(add(5))

sub=lambda a,b,c:a-b-c
print(sub(4,3,2))
print(sub(5,4,-2))
print(sub(2,5,1))
'''

tall_enough=lambda h:h>=175
print(tall_enough(175))
print(tall_enough(160))

#if ; else using lambda
wei_enou=lambda w : "yes" if w>75 else "no"
print(wei_enou(80))
print(wei_enou(70))

#task : square of num's , find cube val , ...
#in lambda can pass "str, list,etc..."

cube=lambda x:x**2
print(cube(2))

cube=lambda x:x**3
print(cube(2))


