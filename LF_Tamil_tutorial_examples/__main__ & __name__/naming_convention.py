'''
Access modifiers:
    public variable - can be accessed at anywhere
    private var - can be accessed only with in that class,using __(double underscore)
    protected var - can be accessed within that class & the inherited classes

also uses  in the method/function
Eg:
class sad():
    def __ref(self):      #by giving like as protected method,this method will able to acces only within that class
        print("sred")     #but,this is not in the correct format
    def sd(color):
        self.__color=color   # procted variable,is also called as Dunder variable

also give as Dunder methods
'''

'''
when it has double underscore in both sides  -  are called as internal variables/methods 
   Eg:def __init__(self):

#some other internal variables :
              __name__    &    __main__   ,etc....
'''
# Eg:
import random
print(__name__)   #in this the  '__main__' will store ; when we call from another file/module it just shows the currentfile name/that module name
def guess_the_no_game():
    if __name__=='__main__':        #when like to execute by calling directly ; give .....  inside like this
        print("you was running this directly....")
    print(__name__)

    num=random.randint(1,30+1)
    guess=int(input("Guess the no?Hint:It is less than 31 - "))
    while guess!=num:
        if guess>num:
            print("Guess is higher")
        if guess<num:
            print("Guess is lower")
        guess=int(input("Guess again:"))
    print("You win,"+str(guess)+" is right")

guess_the_no_game()