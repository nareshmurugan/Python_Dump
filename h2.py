#a=list(map(float,input().split()))
a=[0.4,0.3,0.1,0.1,0.1]
a=sorted(a,reverse=True)
l=[a]
d=[a]
while 1:
    p=round(a[-1]+a[-2],1)
    s=a+[p]
    a=sorted(s,reverse=True)
    l.append(a)
    a[-2:]=[[a[-2],0],[a[-1],1]]
    print(a)
    d.append(a)
    del a[-2:]
    if(len(a)==1):
        break
#for i in d:
#	print(i)
        
