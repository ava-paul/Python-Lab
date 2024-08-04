n=int(input())
for i in range(1,n+1):
    print(i,end=" ")
    r=1
    for j in range(1,5):
        print(r,end=" ")
        r=r*i
    print()
