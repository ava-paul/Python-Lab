n=int(input())
for i in range(n-1):
    print("/",end="")
    if(i==n-2):
        for j in range(n-1):
            print("_",end="")
    else:
        for j in range(i):
            print(" ",end="")
    print("\\")
