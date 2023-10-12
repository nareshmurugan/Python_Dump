import math as m
a=int(input())
l=[]
ll=[]
lll=[]
for i in range(a):
    b=input().split()
    b=list(map(int,b))
    l.append(b)
for j in range(len(l)):
    ll.append(l[j][1])
s=[]
for h in range(int(m.sqrt(max(ll)))):
    s.append(h**2)
for g in ll:
    for d in range(g[0],g[1]):
        
