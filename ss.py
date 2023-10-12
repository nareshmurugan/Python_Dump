import math
n=int(input())
s=input()
p=s.split()
ss=set(s.split())
l=[]
for i in ss:
    l.append(p.count(i))
r=[]
for i in l:
    r.append(math.floor(i/2))
result=0
for i in r:
    result+=i
print(result)
