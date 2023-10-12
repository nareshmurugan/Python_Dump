#a=list(map(float,input().split()))
a=[0.8, 0.7, 0.5, 0.3, 0.2, 0.2, 0.1]
a=sorted(a,reverse=True)
l=[a]
d=[]
for i in range(len(a)):
    p=round(a[-1]+a[-2],1)
    s=a+[p]
    a=sorted(s,reverse=True)
    l.append(a)
    del a[-2:]
    if(len(a)==2):
        break
for j in range(len(l)):
    l[j][-2:]=[[l[j][-2],0],[l[j][-1],1]]
    d.append(l)
    if(len(l)==2):
        break
for k in l:
    print(k)
