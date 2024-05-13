'''
arr=[24,53,12,76,55]
max=arr[0]
for i in range(0,len(arr)):
    if arr[i]>max:
        max=arr[i]
print(f"the peak element among {arr} is",max)
'''

li=[12,34,26,76,98,24,46,24,13]
max=0
for i in range(0,len(li)):
    if li[i]>max:
        max=li[i]
print(f"the peak element of {li} is",max)
