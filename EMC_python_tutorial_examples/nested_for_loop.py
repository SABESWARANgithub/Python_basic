# for i in range(1,5):
#     print("hello")
#     for j in range(1,3):
#         print(j)

# for i in range(1,6):
#     print("\nhello")
#     for j in range(1,3):
#         print(j,end=" ")


# for m in range(1,12+1):
#     print("\n\nMonth - ",m)
#     for i in range(1,5):
#         print("\nWeek - ",i)
#         for j in range(1,7+1):
#             print("day - ",j)


# for i in range(1,4):
#     print("\r")
#     for j in range(1,i+1):
#         print("*",end=" ")
# for i in range(3,0,-1):
#     print("\r")
#     for j in range(1,i):
#         print("*",end=" ")

def py(n):
    for i in range(1,n+1):
        spaces=" "*(n-i)
        stars="*"*(2*i-1)
        print(spaces+stars)
py(5)












