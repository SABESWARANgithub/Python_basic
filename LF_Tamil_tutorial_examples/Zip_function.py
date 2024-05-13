#Zip two or more iterables into a single iteralable
#Eg: l concatinating the two lists into a single list concept;but different

items=("Phone","pen","bag")
prices=(10000,15,300)
zipped=zip(items,prices)
print(zipped)
zipped1=list(zip(items,prices))
print(zipped1)
zipped2=tuple(zip(items,prices))
print(zipped2)
zipped3=set(zip(items,prices))
print(zipped3)
zipped4=dict(zip(items,prices))
print(zipped4)
print("\n")


#we going to give as the data's in list manner ; but even;in output it resembles like list of tuples ; compare with before eg

items=["Phone","pen","bag"]
prices=[10000,15,300]
zipped=list(zip(items,prices))
print(zipped)

#we not only able to zip two list ; can zip more than two list(data's) also
print("\n")
stocks=("out of stock","available-more","available-limited")
zippp=zip(items,prices,stocks)
print(zippp)
zippp1=list(zip(items,prices,stocks))
print(zippp1)
#to zip in dictionary way it not possible ; because the dict only contain like key & values data's only ;
#                                                                  it shows error while zip three data's in dict way
# zippp2=dict(zip(items,prices,stocks))
# print(zippp2)

# if we not mention/given is in one missing data way ;see & compare the outputs
stocks1=["out of stock","available-more"]
zipppp=list(zip(items,prices,stocks1))
print(zipppp)

