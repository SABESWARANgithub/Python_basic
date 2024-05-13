
'''                 #Map............
  #syntax : map(function,iterable)
#when to like to convert only the price value from the list from INR to USD to get a updated new list from the below list
  # INR value to convert in USD : INR value/74

items=[(23657453,"apple",120),(536516,"mango",40),(386942,"grapes",80)]
inr_usd=lambda item:(item[0],item[1],item[2]/74)
fin_items=list(map(inr_usd,items))
print(fin_items)

# the USD value upto 2 digits
inr_usd1=lambda item:(item[0],item[1],float("{:.2f}".format(item[2]/74)))
fin_items1=list(map(inr_usd1,items))
print(fin_items1)

# when like to remove the particular value itself
inr_usd2=lambda item:(item[1],float("{:.2f}".format(item[2]/74)))
fin_items2=list(map(inr_usd2,items))
print(fin_items2)

#task - to square the val in list
val=[1,2,3,4,5]
sqr=lambda item:item**2
m=list(map(sqr,val))
print(m)

#another method
   #when we not not convert the object to list it just shows that object addres code
val1=[6,7,8,9]
va1=map(lambda x:x**2,val1)
print(va1)

val1=[6,7,8,9]
va1=list(map(lambda x:x**2,val1))
print(va1)

# before eg without using lambda function
def sqr(num):
    return num*num
sq_val=list(map(sqr,val1))
print(sq_val)

#tasks
     #subject name,student name,mark for 200
student=[("maths","ram",170),("science","sam",167),("science","ram",198),("maths","sam",178)]
st=lambda y:(y[1],y[2]/2)
ts=list(map(st,student))
print(st)

val3=[73,71,64,97,34]
s=lambda x:"even" if x%2==0 else "odd"
ms=list(map(s,val3))
print(ms)

#farenheit to celsius formula - (n-32)*5/9
temp=[104,79,207]
cel=lambda c:(c-32)*5/9
far_cel=list(map(cel,temp))
print(far_cel)

cel1=lambda c:float("{:.2f}".format((c-32)*5/9))
far_cel1=list(map(cel1,temp))
print(far_cel1)
'''

'''
          #Filter
  #syntax :  filter(function,iterable)

items=[(23657453,"apple",120),(536516,"mango",40),(386942,"grapes",80)]
lees_than_100=lambda x:x[2]<100
filtered1=filter(lees_than_100,items)
filtered=list(filter(lees_than_100,items))
print(filtered1)
print(filtered)

#filter te items; which are only starting with "g"
filtered_g=list(filter(lambda y:y[1][0]=="g",items))
print(filtered_g)


#assignment

#filter items by the code no's range b^n 2000 to 5000
items=[(2354,"apple",120),(7643,"mango",40),(4763,"grapes",80)]
fil_2000_5000=list(filter(lambda k:k[0]>2000 and k[0]<5000,items))
print(fil_2000_5000)

#filter by name & mark
stud_detail=[("maths","Anand",74),("science","ram",68),("maths","Anandhi",56),("science","Abi",87)]
fil_stu=list(filter(lambda s:s[1][0]=="A" and s[2]>70,stud_detail))
print(fil_stu)
'''

         #reduce
  #syntax - reduce(function,iterable) ; performs the func on/of two elements & repeats it until it transforms the list of values into a single/one value remains on the iterable
  #to use reduce "import the module"
import functools
list1=[1,3,4,6,8]
list2=[3,4,5,6,75,6,7,22]
sum=functools.reduce(lambda x,y:x+y,list1)
sum1=functools.reduce(lambda x,y:x+y,list2)
print(sum)
print(sum1)

alps=["s","a","b","e","s"]
sing=["S","i","n","g","l","e"," ","T","a","m","i","l","a","n"]
joined_name=functools.reduce(lambda a,b:a+b,alps)
joined_sing=functools.reduce(lambda a,b:a+b,sing)
print(joined_name)
print(joined_sing)



