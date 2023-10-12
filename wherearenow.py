s=[i_ for i_ in range(1,1000)]
t=int(input())
tc=[]
s=[1,2,3,4,5]
for j_ in range(t):
    tcs=input().split()
    tcl=list(map(int,tcs))
    tc.append(tcl)
g=[]
for k in range(len(tc)):
    g.append(tc[k][0])
nn=2
for y in range(len(g)):
    n=g[y]
    i=0
    for i in s:
        for j in range(nn,n+1):
            print(i&j,i,j)
            nn+=nn
            n-=n

    
