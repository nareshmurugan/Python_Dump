a=list(map(int,input().split()))
l=[]
for i in range(a):
    b=input()
    l.append(b)
print(len(set(l)))
f=set(l)
ll=[l.count(l[x]) for x in range(len(f))]
for j in ll:
    print(j,end=' ')
