#using while is correct,then only it loop again & again
'''
import random
num=random.randint(1,30+1)
guess=int(input("Guess the no?Hint:It is less than 31 - "))
while guess!=num:
    if guess>num:
        print("Guess is higher")
    if guess<num:                          #also use else,instead of if
        print("Guess is lower")
    guess=int(input("Guess again:"))
print("You win,"+str(guess)+" is right")
'''


#Wrong - not loop again & again,even the guess is wrong
'''
import random
num=random.randint(1,30+1)
guess=int(input("Guess the no?Hint:It is less than 31 - "))
if guess!=num:
    if guess>num:
        print("Guess is higher")
    if guess<num:
        print("Guess is lower")
    guess=int(input("Guess again:"))
print("You win,"+str(guess)+" is right")'''

  #Task-1
  '''
import math
n=int(input("Enter no: "))
fact=1
while n>=1:
    fact=fact*n
    n=n-1
print(fact)'''


#task-2  - to do list
# l=[]
# class Todo():
#     def add(self):
#         a=input("Enter anything:")
#         l.append(a)
#     def dele(self):
#         l.pop()
#     def final(self):
#         print(list(l))
# td=Todo()
# td.add()
# td.add()
# td.add()
# td.final()
# td.dele()
# td.final()
