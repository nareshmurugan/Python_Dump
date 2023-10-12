N=int(input())
l=input().split()
l=list(list(map(int,l)))
p=[]
n=[]
z=[]
for i in l:
    if(i>0):
        p.append(i)
    elif(i<0):
        n.append(i)
    elif(i==0):
        z.append(i)
print("%1.6f"%(len(p)/N))
print("%1.6f"%(len(n)/N))
print("%1.6f"%(len(z)/N))
