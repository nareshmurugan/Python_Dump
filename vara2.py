a=int(input())
b=int(input())
l=[x for x in range(a+1)]
n=2
r=[l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n )]
s=[]
for i in r:
    if(b in i):
        #print(r.index(i))
        s.append(r.index(i))
if(len(r[-1])==1):
    l=l[::-1]
    l.insert(1,0)
else:
    l=l[::-1]
_r=[l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n )]
for i in _r:
    if(b in i):
        #print(_r.index(i))
        s.append(_r.index(i))
print(min(s))
