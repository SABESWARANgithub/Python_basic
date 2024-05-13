'''
           #basic sorting eg's:
cities=["salem","chennai","madurai"]
val=[2,1,4,6,3,9,5]

  #temporary sort
print(sorted(cities))
print(sorted(val))
                                     #  sorted -by using this function; tempporarily can sort
print(cities)
print(val)

  #permanent sort
val.sort()
print(val)
                       #  .sort() - by using this method ;can permanently sort
cities.sort()
print(cities)

   #reverse
s=[1,3,2,5,7,3,5,1]

print(sorted(s))
print(s)

s.reverse()
print(s)
'''

    #sorting with key

#going to crreate list of tuple's
    #itemcode,itemname,price
item=[(24563,"banana",28),(3588,"apple",120),(25897,"orange",80)]       #in this list, there are 3 tuples; can give many as we need

item.sort()        #it just sort by the itemcode ; (1st value of tuple)
print(item)

#when we like to sort by itemname,price (or) by specifically mentioning the keys
 # want to code using with lambda keyword or function

item1=[(24563,"banana",28),(3588,"apple",120),(25897,"orange",80),(5654,"grapes",70)]
item1.sort(key=lambda item:item[1])
print(item1)
item1.sort(key=lambda item:item[2])
print(item1)

#sort in desencing order
item1.sort(key=lambda item:item[2],reverse=True)
print(item1)

#task
students=[("maths","ram",70),("science","sam",60),("science","ram",50),("maths","sam",75)]
students.sort(key=lambda item:item[0])
print(students)

students.sort(key=lambda item:item[1])
print(students)

students.sort(key=lambda item:item[2])
print(students)

# tuple are not able to modify ; to modify tuple ,change the tuple into list & then modify it
 #also use sorted function ; to modify the tuple
        #tuple of tuples
fruits=((24563,"banana",28),(3588,"apple",120),(25897,"orange",80),(5654,"grapes",70))
print(sorted(fruits))
print(fruits)

  #when like to 'sort with key' in tuple of tuples
print(sorted(fruits,key=lambda item:item[2]))
print(sorted(fruits,key=lambda item:item[2],reverse=True))

#task - sort the previous task data to sort by using sorted function

students=[("maths","ram",70),("science","sam",60),("science","ram",50),("maths","sam",75)]
print(sorted(students,key=lambda sr:sr[2]))
print(sorted(students,key=lambda sr:sr[2],reverse=True))