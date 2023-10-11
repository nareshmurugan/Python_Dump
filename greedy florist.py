n,k=list(map(int,input().split()))
c=sorted(list(map(int,input().split())),reverse=True)
if(k==n):
    count=sum(c)
else:
    count=0
    for i in range(1,k):
        count+=c[i]
    for j in c[i:]:
        count+=j*2
print(count)
        
    
