# i=1                  #run for infinite times
# while(i<=5):
#     print(i)

# i=True
# while(i==True):      #run for infinite times
#     print("hi")

# i=0
# while(i<=100):
#     print(i,end=","" ")
#     i=i+10

# i=10
# while(i>=1):
#     print(i,end=" ")
#     i=i-1

'''
a=int(input("Enter a num to find factorial:"))
fact=1
while(a>=1):
    fact=fact*a
    a=a-1
print(fact)
'''



letter=input("Enter the data:")
while not letter.isalpha():
    letter=input("Enter only letters:")
print("you have entered,",letter)
