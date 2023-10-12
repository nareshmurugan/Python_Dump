import numpy as n
#x,Y=int(input("ENTER THE NUMBER OF ROWS")),int(input("ENTER THE NUMBER OF COLUMNS"))
a,b,c=str(input("ENTER THE FIRST ROW IN SERIOUS:")),str(input("ENTER THE SECOND ROW IN SERIOUS:")),str(input("ENTER THE THIRD ROW IN SERIOUS"))
print(a,b,c,end='\n')
d,e,f=a.split(),b.split(),c.split()
l=(int(d[0]),int(d[1]),int(d[2]))
k=(int(e[0]),int(e[1]),int(e[2]))
m=(int(f[0]),int(f[1]),int(f[2]))
g=n.array([l,k,m])
print("THIS IS THE GIVEN ARRRAY\n",g)
if(l[0]!=1):
    if(k[0]==1):
        g=n.array([k,l,m])
    elif(m[0]==1):
        g=n.array([m,k,l])
else:
    g=n.array([l,k,m])
print(g)
r1,r2,r3=g[0],g[1],g[2]
rc1=g[0,0]*r2/g[1,0]*r1
g[0]=rc1
rc2=g[1,0]*r3-g[2,0]*r2
g[1]=rc2
rc3=r1*g[2,0]-r3
g[2]=rc3
print(g)
rc4=g[1,1]*r3-g[2,1]*r2
g[2]=rc4
print(g)
