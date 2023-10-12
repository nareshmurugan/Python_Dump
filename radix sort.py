l=[81,94,115,926,112,5,107,935,2338,528,3233,3,3333]
#l=list(map(int,input().split()))
m=len(str(max(l)))
l=list(map(str,l))
for i in range(len(l)):
    if(len(l[i])!=m):
        l[i]=abs(len(l[i])-m)*'0'+l[i]
ll=[]
for i in range(-1,-(m+1),-1):
    o=[]
    p=[[] for y in range(10)]
    for j in range(len(l)):
        p[int(l[j][i])].append(l[j])
    for jj in p:
        o.extend(jj)
    l=o
    p=[]    
o=list(map(int,o))
print("In the end of radix sort :",o) 
    
