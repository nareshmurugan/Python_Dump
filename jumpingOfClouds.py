nOC=int(input())
aOC=input().split()
aOC=list(list(map(int,aOC)))
index=0
jump=0
n=2
r=[l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n )]
s=[]
for i in r:
    if(b in i):
        #print(r.index(i))
        s.append(r.index(i))
    
