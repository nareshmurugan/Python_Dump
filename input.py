import numpy as n
a=str(input("enter the number as series:"))
b=str(input("enter the number as series:"))
c=str(input("enter the number as series:"))
print(a,b,c,end='\n')
d=a.split()
e=b.split()
f=c.split()
g=n.array([(int(d[0]),int(d[1]),int(d[2])),(int(e[0]),int(e[1]),int(e[2])),(int(f[0]),int(f[1]),int(f[2]))])
print(g)
