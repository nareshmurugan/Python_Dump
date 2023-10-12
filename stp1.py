#save the prisioner
def sP(np,nc,sc):
    re=sc+nc-1
    re%=np
    if(re==0):
        return n
    return re
n=int(input())
l=[list(map(int,input().split())) for j in range(n)]
for k in l:
    print(sP(k[0],k[1],k[2]))
