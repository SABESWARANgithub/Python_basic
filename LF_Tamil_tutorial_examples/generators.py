'''
use "yield" keyword instead of using return,while like to use generators
when we like to give the data's in the list format,it occupy's more memory(space),in that time;we use generators
the data scientists & data analysts mostly use this generators to handle large amount of data's
'''

#basic eg - without generator
def sq_nums(num):
    sq=[]
    for i in range(1,num+1):
        sq.append(i*i)
    return sq
print(sq_nums(6))

#eg with generators
def sq_nums_gen(num):
    for i in range(1,num+1):
        yield i*i
generator=sq_nums_gen(6)
for i in generator:
    print(i,end=",")




