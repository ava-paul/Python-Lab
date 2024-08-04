n=int(input())
sum=0
sign=1
for i in range(1,n+1):
    sum+=1/(i*sign)
    sign*=(-1)
print(sum)
    
