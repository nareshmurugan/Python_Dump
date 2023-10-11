nOC=int(input())
aOC=input().split()
aOC=list(list(map(int,aOC)))
index=0
jump=0
for i in aOC[1:]:
    if(i==1 and i!=1):
        index+=1
    if(i==0 and i!=1):
        index+=1
print(index)
    
