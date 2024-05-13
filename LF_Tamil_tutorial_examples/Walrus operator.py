#walrus operaor - ":=" colon-equal_to is a walrus operator
#use walrus operator;when we like to assign & also use to do extra work check or comparision function/operation ;
#                             ... when do another/extra work use this operator
'''
basic eg:
    name="varun"
    print(name)     output: varun

    if we try to given in single line as,

     print(name="varun")       error message shows
'''

#print(name := "varun")             #operator used is walrus operator
'''
      # before used Eg:
      
print("enter list of numbers:hint-'Enter z to end'")
list_num=[]
while True:
 inp=input()
 if inp=="z":
  break
 list_num.append(inp)
print(list_num)
'''

#minimize the before eg: code using walrus operator

print("enter list of numbers:hint-'Enter z to end'")
list_num=list()
while (inp := input()) !='z':
    list_num.append(inp)
print(list_num)
