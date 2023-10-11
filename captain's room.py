a=int(input())
b=set(map(int,input().split()))
print(max(b))
'''
c=set(b)
c=list(c)
l=[]
for i in range(len(c)):
    l.append(b.count(c[i]))
print(c[l.index(min(l))])
'''
