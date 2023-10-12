l=[275,87,426,61,509,170,677,503]
#l=list(map(int,input().split()))
m=len(str(max(l)))
l=list(map(str,l))
#converting all the number into max numbers digit count by adding zero
for i in range(len(l)):
    if(len(l[i])!=m):
        l[i]=abs(len(l[i])-m)*'0'+l[i]
#############################################
#Radix Sort
print("###################Radix Sort###################")
ll=[]
for i in range(-1,-(m+1),-1):
    o=[]
    p=[[] for y in range(10)]
    for j in range(len(l)):
        p[int(l[j][i])].append(l[j])
    for jj in p:
        o.extend(jj)

    print(f'\nPass {-i}: {list(map(int,o))}')
    l=o
    p=[]    
o=list(map(int,o))
print(f'\nIn the end of radix sort : {o}') 
#############################################    
    
