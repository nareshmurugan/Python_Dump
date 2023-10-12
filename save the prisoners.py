def sP(np,nc,sc):
    p=[i for i in range(1,np+1)]
    pp=p[p.index(sc):]
    for i in pp:
            nc-=1
            if(i==pp[-1]):
                    pp.extend(p)
            if(nc==0):
                    break
    return i
n=int(input())
l=[list(map(int,input().split())) for j in range(n)]
for k in l:
    print(sP(k[0],k[1],k[2]))
