a=int(input())
b=input().split()
b=list(map(int,b))
c=set(b)
l=[]
d=0
k=[]
for i in c:
   l.append({i,b.count(i)})
   k.append(b.count(i))
   d+=1

f=max(l)
h=list(c)
print(h[k.index(max(k))])

