#string slicing
para="the world is going to destroy"
print(para[6:])
print(para[0:7])
print(para[:12])
print(para[1:15:2])          #from this line;upto the last print function,all the last number are just pointing the "step count"
print(para[-1:-15:-2])
print(para[:8:-3])
print(para[:8:3])


#string split
a="red,blue,green,yellow"
n=a.split(",")                   #want to assign the split method to any variable as "n" used here,then only split will use
print(n)

a="red blue green yellow"
n=a.split(" ")                   #want to assign the split method to any variable as "n" used here,then only split will use
print(n)


#string join
a="red"
n="-".join(a)                   #want to assign the split method to any variable as "n" used here,then only split will use
print(n)