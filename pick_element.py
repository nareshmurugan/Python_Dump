import itertools as it
a=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(2,len(b)):
    for j in it.permutations(b,i):
        l.append(j)

ll=set(set(i) for i in l)
g=[]
for i in set(ll):
    p=[]
    for j in range(2):
        p.append(i)
    g.append(p)
            
