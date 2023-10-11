import string as s
ss=s.ascii_lowercase
a=list(map(int,input().split()))
b=list(input())
c=list(ss)
d=list(zip(a,c))
l=[]
for i in b:
    l.append(d[ss.index(i)][0])
print(max(l)*len(b))
