
#search in any search engine "python module list" - to see various types of modules to use as our need
'''
 - import math - math is one type of module
eg: in one folder;we create many python files, each files are called as module
eg: when we like to call the function,which is in another file(module);we want to import that module(file) to the file,where we going to call
'''

import email              #this is the best method to access,to mention specific to call the function,...
print(email.otp())         #     then only the conflits will not come
print(email.activate())
print("\n")

import email as e
print(e.otp())
print(e.activate())
print("\n")

#another method
from email import otp           #by this method,we can able to import only one function from that module(file)
print(otp())
print("\n")
#to access the more functions from the module by the before method
from email import otp,activate
print(otp())
print(activate())
print("\n")

#to access all functions in that module(file) by before method
from email import *
print(otp())                #but don't use this way of accessing all iin that file mostly
print(activate())