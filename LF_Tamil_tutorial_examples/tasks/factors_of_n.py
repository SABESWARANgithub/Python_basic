#factors of n is states as;the n value is divisible by any number,for which numbers get
# the remainder of zero are called as factors of n

n=int(input("enter the number:"))
print(f"the factors of {n} are,")
for i in range(1,n+1):
    if (n%i==0):
        print(i,end=",")