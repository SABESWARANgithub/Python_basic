'''
higher_order_function : when one func gets the argument/parameter as the another one functionn itself is
                                                               (or) returns a function called higher order function
in the below example  ;   feeling() & minnd() - functions are known as the *** higher order func ***
'''

'''
#basic eg:
def happy():
    print("Jumping...")
def sad():
    print("Crying...")
print(happy())     #output - jumping....
print(happy)        #output - <function happy at 0x00000186F59DC540> ; it give some address code, where that happy func is located
                     #the address code is change each & every time ; when we run every time

joy=happy()        #assigning the happy() funnc to a new/another variable
print(joy)             #output - jumping....

hey=happy             #  ***not giving () in last is right
hey()                 #output - jumping....

print(sad)
sorrow=sad
sorrow()



# gets the argument/parameter as the name of another one of the function
def feeling(func):
    func()

def mind(func):
    func

mind(sad())
'''

#returning function
def calm_down():
    print("calm down")

def happy():
    print("Jumping...")

def sad():
    print("Crying...")

# gets the argument/parameter as the name of another one of the function
def feeling(func):
    func()
    return calm_down

func= feeling(happy)
func()
func2=feeling(sad)
func2()

def mind(func):
    func

mind(sad())



