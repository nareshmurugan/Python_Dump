import math
n=int(input())
s=input()
ll=s.split()
a=[]
for i in range(len(ll)):
    a.append(s.count(ll[i]))
aa=set(a)
r=[]
for i in aa:
    r.append(math.floor(i/2))
result=0
for i in r:
    result+=i
print(result)
