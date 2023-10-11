aa=int(input())
a=list(map(int,input().split()))
bb=int(input())
b=list(map(int,input().split()))
lr=[]
lnr=sorted(list(set(a)),reverse=True)
r=[h for h in lnr]
rr=[f for f in range(1,len(lnr))]
for i in r:
    for j in range(len(r)):
        print(i,b[j])
