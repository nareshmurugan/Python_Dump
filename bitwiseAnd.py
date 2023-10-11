s={i_ for i_ in range(1,1000)}
t=int(input())
tc=[]
for j_ in range(t):
    tcs=input().split()
    tcl=list(map(int,tcs))
    tc.append(tcl)
tu=[]
for v in range(len(tc)):
    tu.append(tc[v][0])
for r in tu:
    def bitwiseAnd(r):
        global tc,t,s
        nn=2
        dhiya=[]
        l_=0
        ln=len(s)
        g=[]
        for k in range(len(tc)):
            g.append(tc[k][0])
        for i in s:
            for h in g:
                for j in range(nn,h+1):
                    dhiya.append(i&j)
                    nn+=nn
                    h-=h
            ln-=1
            if(i==t):
                break
        return dhiya
    print(bitwiseAnd(r))
