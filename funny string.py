a=int(input())
r=[]
for i in range(a):
    b=list(input())
    l=[ord(i) for i in b]
    dl=[];s=0;t=1
    for j in range(len(b)-1):
        dl.append(abs(l[s]-l[t]))
        s+=1;t+=1
    r.append("Funny") if(dl==dl[::-1]) else r.append("Not Funny")
for j in r:
    print(j)
