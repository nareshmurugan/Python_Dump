aa=int(input())
a=list(map(int,input().split()))
bb=int(input())
b=list(map(int,input().split()))
lr=[]
lnr=sorted(list(set(a)),reverse=True)
r={j:i for i,j in enumerate(lnr,1)}
rr=[]
for i in r:
    for j in range(len(r)):
        print(i,b[j])
