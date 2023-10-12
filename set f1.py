n=int(input("Enter the count of elements"))
ne=input("Enter the elements").split()
nel=set()
nel1=set()
o_=['intersection_update','update','symmetric_difference_update',
        'difference_update']
for i in range(len(ne)):
    nel.add(int(ne[i]))
nele=nel
nelem=int(input("Enter the number of operations"))
a=[]
for j in range(nelem):
    neleme=input("Enter the operation and number elements to perform with elements").split()
    nelemen=input("Enter the elements to the operation").split()
    for k in range(len(nelemen)):
        a.append(neleme)
    for m in range(len(nelemen)):
        nel1.add(int(nelemen[m]))
    nelemen=nel1
print(n,ne,nel,nele,nelem,neleme,nelemen,end='\n')
for n in range(len(o_)):
        nn=nel
        if(o_[n]=='intersection_update'):
            n1=nn.intersection_update(nelemen)
        n1=nn    
        if(o_[n]=='update'):
            n1=nn.update(nelemen)
        n1=nn    
        if(o_[n]=='symmetric_difference_update'):
            n1=nn.symmetric_difference_update(nelemen)
        n1=nn    
        if(o_[n]=='difference_update'):
            n1=nn.difference_update(nelemen)
        n1=nn    
print(sum(nele))
