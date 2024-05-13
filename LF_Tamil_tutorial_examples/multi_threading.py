'''
import threading
print(threading.active_count())

output : 1   ;   it means that now it has only one thread

          to known about thread is that ;
print(threading.enumerate())

output : [<_MainThread(MainThread, started 8604)>]  ;  it means the main thread only running now

upto now the prg's which had we used to code are basically run with/by the main thread only
'''

'''
import threading

def update_db():
    print("Updating data base")
update_db()

print(threading.active_count())
print(threading.enumerate())
'''

'''
#when we like to update the db ;it takes some time   -  we can also introduce that time delay in an eleberate way by importing the module
import threading
import time

def update_db():
    print("Updating data base")
    time.sleep(5)                 #when we give like this it wont do anything for 5 seconds
    print("updated db")

def display_nums(num):
    for i in range(1,num+1):
        print(i,end=",")

update_db()
display_nums(20)

print("\n",threading.active_count())     #shows no.of threads are there
print(threading.enumerate())        #shows which thread is running
'''

'''
while updating database ;when there is delay time in updating the db -- the next/following process will get's affected by giving output
---if we don't like to delay the following processes  ; even there is delay time before
-----then only the following task will processes in a proper way (like to process the following task;even there is a delay timing in the thread of database to update it)

----give that func/... in another thread; which have the dalay time (then only it womn't affect the process in the proper way of processing the following/next ;the database thread will do their process to take their own time ; )
  ---like this we can give many threads ; is called as "multi-threading"
'''

import threading
import time

def update_db():
    print("Updating data base")
    time.sleep(5)                    #when we give like this it wont do anything for 5 seconds
    print("updated db")

def display_nums(num):
    for i in range(1,num+1):
        print(i,end=",")

#update_db()    --don't call like this directly insteadcall as..... ; while using threading / multi-threading
threading.Thread(target=update_db())      #module.method( mention which method to target by that thread ,we can also give the required arguments if have )
#the above line is used to ready&make a thread and give; we call store it in a particular variable
display_nums(20)

print("\n",threading.active_count())     #shows no.of threads are there
print(threading.enumerate())

