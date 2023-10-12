n=int(input("Enter the count of elements"))
ne=input("Enter the elements").split()
nel=set()
nel1=set()
o_=['intersection_update','update','symmetric_difference_update',
        'difference_update']
for i in range(len(ne)):
    nel.add(int(ne[i]))
nelem=int(input("Enter the number of operations"))
for j in range(nelem):
    neleme=input("Enter the operation and number elements to perform with elements").split()
    nelemen=input("Enter the elements to the operation").split() 
    for n in range(len(o_)):
        if(o_[n]=='intersection_update'):
            nel.intersection_update(nelemen)
        elif(o_[n]=='update'):
            nel.update(nelemen)
        elif(o_[n]=='symmetric_difference_update'):
            nel.symmetric_difference_update(nelemen)
        elif(o_[n]=='difference_update'):
            nel.difference_update(nelemen)
print(sum(nel))
