import math as m
#l=[81,94,11,96,12,35,17,95,28,58]
l=list(map(int,input().split()))
s=2
while 1:
    k=m.ceil(len(l)/s)
    u=k
    for i in range(len(l)):
        if(u==len(l)):
            continue
        if l[i]>l[u]:
            l[i],l[u]=l[u],l[i]
        u+=1
    s=s*2
    if k==1:
        break
for j in range(len(l)-1):
    if l[j]>l[j+1]:
        l[j],l[j+1]=l[j+1],l[j]
print(l)
