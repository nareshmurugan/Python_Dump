s={i_ for i_ in range(1,1000)}
t=int(input())
tc=[]
for j_ in range(t):
    tcs=input().split()
    tcl=list(map(int,tcs))
    tc.append(tcl)
g=[]
for k in range(len(tc)):
    g.append(tc[k][0])
for y in g:
    
    tu=[]
    nn=2
    dhiya=[]
    l_=0
    ln=len(s)
    for i in s:
        for h in g:
            for j in range(nn,h+1):
                dhiya.append(i&j)
                nn+=nn
                h-=h
                ln-=1
    return dhiya
c=[]
for b in g:
    print(bitwiseAnd(b))
