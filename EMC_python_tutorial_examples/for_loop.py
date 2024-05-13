'''
list=[1,2,3,4]
for i in list:
    print(i)

for i in range(2,6):
    print(i)

for i in range(5):
    print(i)

for i in range(2):
    print(i,"hi")
    print("hello")

a=int(input())
b=int(input())
for i in range(a,b):
    print("h")

count=0
for i in range(1,10+1):
    if(i%2==0):
        print(i)
        count+=1
print(count)
'''

'''
cou=0
a=int(input("a:"))
b=int(input("b:"))
for i in range(1,45):
    if(i%3==0 and i%7==0):
        print(i,end=" ")
        cou+=1
print("\nCou:",cou)
'''


even_count=0
odd_count=0
print("Even no's:")
for i in range(0+1,10+1):
    if(i%2==0):
        print(i,end=",")
        even_count+=1

print("\nOdd no.s:")
for i in range(0+1,10+1):
    if(i%2!=0):
        print(i,end=",")
        odd_count+=1

print("\n\nEven no.s:",even_count)
print("Odd no.s:",odd_count)


# n=int(input(("No of terms:")))
# for i in range(1,n+1):
#     print("No is:",i,"& its cube is:",i**3)




