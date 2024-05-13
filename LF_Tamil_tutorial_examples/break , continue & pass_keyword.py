'''
#break
list_num=[]
while True:                  #Mostly give the "break" inside the if statement only
    a=input()
    if a=='s':                #if there is break;if we give else,it won't execute
        break
    list_num.append(int(a))
print(list_num)
'''

'''
#continue  -  continues to the next iteration
str1="a,b,c,d"
str2=""
for i in str1:
    if i==",":
        continue
    str2=str2+i
print(str2)
print(list(str2))
'''

#pass  -  do noting

''' pass is a null operation — when it is executed, nothing happens. 
It is useful as a placeholder when a statement is required syntactically, 
but no code needs to be executed'''

str1="a,b,c,d"
str2=""
for i in str1:
    if i==",":
        pass
    else:                  #if we give else;get the same output as before eg
        str2=str2+i
print(str2)                #otherwise,we get :Ouput as  -  a,b,c,d
print(list(str2))          #                               ['a', ',', 'b', ',', 'c', ',', 'd']


