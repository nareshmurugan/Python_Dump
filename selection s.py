a=list(map(int,input().split()))
le=len(a[:])
l=[]
j=0
while(j<le):
    a[a.index(min(a))],a[0]=a[0],min(a)
    l.append(a[0])
    del a[0]
    j+=1
print("The sorted array is:\t",l)
