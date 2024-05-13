'''mode:"r+" - use to read/write/add/append
    "w" - use to add/write/update data's       #using apppend is best option instead of using write
     "r" - use to read data                    #if use write,the current value only store "which value is associated by write" ,the data's/values which was already have will deleted
     "a" - use to add/append data            #but when use append,it just append/add the data only,not delete/remove the data's which was already have
'''
#one method
'''
f=open("fruits.txt","r+")
print(f.read())
print(f)                        #when we open file must close; while using this type of file handling method
f.write("pineapple")
f.close()'''


#another method - using with & as keyword

with open("fruits.txt","r+") as file:      #instead of file(name) can give any name
    print(file.read())                  #???by using this method don't need to close file,automitacally close by itself
    print(file.mode)
    file.write("Grapes")
    print(file.name)
    print(file.readable())
    print(file.read())
    file.close()
    print(file.closed)

