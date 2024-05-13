#list[],tuple(),set{},dictionary{key-value pairs}

#list - allow duplicate,modify
'''
a=[1,2,3,4,5,6,7]
print(a)
a.append("hi")
print(a)
a.insert(0,0)  #add 0 in 0th position
print(a)
a.pop()
print(a)
a.pop(1)
print(a)
del a[2]      #if use del keyword;mention the index value
print(a)
deleted=a.pop()
print("the removed value is",deleted)
print(a)

a=[1,2,1,3]
b=[4,5,6]
a.extend(b)      #to concat a and b
print(a)

     #Sorting
cities=["Madurai","salem","Chennai"]
values=[1,3,5,8,2,3,1]
cities.sort()
print(cities)
# print(values.sort())        -for this the output will show as "None"
print(sorted(values))          #this only shows the correct output
'''

#2-dimentional list

'''
cities=["madurai","salem","chennai"]
tn=cities                                # instead of copying(assigning) the data like this,
karnata=["bangalore","mysore"]           #     use "shallow copy / deep copy"
india=[tn,karnata]                       #               Eg: tn=cities[:] / tn=cities.copy()
print(india)
print(india[0])           
print(india[1][1])

cities=["madurai","salem","chennai"]
tn=cities[:]
karnata=["bangalore","mysore"]              # also  by use the module & method.() :   
india=[tn,karnata]                       #   Eg: import copy
print(india)                             #       tn=["madurai","salem"]
print(india[0])                         #        cities=copy.deepcopy(tn)
print(india[1][1])                      #        print(cities)

cities=["madurai","salem","chennai"]
tn=cities.copy()
karnata=["bangalore","mysore"]
india=[tn,karnata]
print(india)
print(india[0])
print(india[1][1])
'''

#tuple - allow duplicate but cannot modify - only modify by using casting
'''
a=(1,2,3,4,"hi")
b=(1,2,1,2,1,3,1,4,1,1,2,2)
a=list(a)
a.pop()                 #can't able to change the particular value in tuble,but able to change the whole values
print(a)
a.insert(0,7)
print(a)
b=list(b)
a.append(b)
print(a)
print(a[0])
print(a.index(2))
print(a[5])
a=(36,43,56)
print(a)
    #to count
print(b.count(1))
li=(1,2,3,1,5,1,6,1)
count=0
for i in li:
    if i==1:
        count=count+1
print(count)

     #to find
sam=(1,2,3,4,5,6,1)
if 3 in sam:
    print("yes")
else:
    print("no")

# to find,it has elements or not
sd=("fghg","gfghfhj","gfhgk")
if sd:
    print("it has elements")
else:
    print("no")

ds=()
if ds:
    print("it has elements")
else:
    print("it has no elements")
'''

#set - not allow duplicate,can't modify,but use add/remove/update/pop,they are unordered

a={1,1,1,2,2,3,4}
print(a)
a.remove(1)
print(a)
a.add("hi")
print(a)
a.pop()
print(a)
b={"a","s","d"}
b.update("f")
print(b)
print(a.pop())
print(a)
print(b.pop())
print(b)
colors={"red","green","blue","black"}
print(colors)                             #set are not used to give in ordered format
#to change the set to list
colors_list=list(colors)
print(colors_list)


#dictionary - not allow duplicate,methods-keys(),values(),items(),get() /update/pop
'''
person_1={
    "name":"Ram",
    "ph_no":545768
}
print(person_1.keys())
print(person_1.values())
print(person_1.items())
print(person_1.get("name"))
print(person_1["ph_no"])
person_1["age"]=21       #add/update
print(person_1)
person_1.update({"job":"speaker"})
person_1.update({"age":35})
print(person_1)
person_1.pop("ph_no")
print(person_1)

#looping in dictionary
p1={
    "name":"Ram",
    "age":27,
    "height":175,
    "district":"salem",
    "state":"Tamilnadu"
}
for key,val in p1.items():
    print("key:",key)
    print("val:",val)
for key in p1.keys():
    print(key,end=",")
print("\n")
for val in p1.values():
    print(val,end=",")
#to arrange in order
for key,val in sorted(p1.items()):
    print(key,val)
for key in sorted(p1.keys()):
    print(key)

#to store single user details in dict. is easy,but when to store multiple user details use "list of dictionaries"
users=[]
user={"name":"Ram","age":21}
users.append(user)
print(users)
user={"name":"lang","age":23}           # not able modify by this method,use .update method to modify
print(users)
user={"name":"gautham","age":34}
users.append(user)
print(users)
print(users[0]['age'])
print(users[1]["name"])

user["fav_food"]="poori"       #to asssign single val to a key
print(user)

user["fav_food"]=["poori","dosa","biriyani"]     #to assign multiple val's to key use list in dictionary
print(user)                                         #get output in list format
user["fav_food"]="poori","dosa","biriyani"
print(user)                                         #get output in tuple format
'''