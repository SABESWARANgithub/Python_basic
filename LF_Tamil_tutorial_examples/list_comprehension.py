#basic eg for sqr values from 1 to 10 ; using for loop
for i in range(1,11):
    print(i*i,end=",")

print("\n")

#before eg with map & lambda function
sqr_val=list(map(lambda x:x*x,range(1,11)))
print(sqr_val)


#.........before eg using list comprehension.............
      #syntax: list=[expression for item in iterable]

val=[2,4,5,7,8,3]
sq=[y*y for y in val]
sqr=[x*x for x in range(1,11)]
print("\n")
print(sq)
print(sqr)

#list comprehension using if condition ; to filter values less than 30
    #syntax: [exprn for item in iterable if cond]
v=[22,44,66,32,39,97,28]
vf=[z for z in v if z<40]
print(vf,"\n")
vf.sort()
print(vf)
print(sorted(v))

#if like to add with else statement
       #syntax: list=[exprn if-else for item in iterable]
v=[22,44,66,32,39,97,28]
vff=[s if s<40 else "?" for s in v]
print(vff)
vv=[s if s<40 else 0 for s in v]
print(vv)



