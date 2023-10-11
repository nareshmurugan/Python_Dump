'''
Karnaugh map
'''
#f=list(map(int,input().split()))
f=[1,4,8,12,14,2]
#a=input("Enter the variables space seperated:\t").split()
a=list("ABCD")
terms=len(a)**2
b=['00','01','11','10'] 
l=[]
for i in b:
    ll=[]
    for j in b:
        ll.append(i+j)
    l.append(ll)
bi=[8,4,2,1]
e=[]
for ii in l:
    ee=[]
    for jj in ii:
        c=0
        for kk in range(len(jj)):
            if(jj[kk]=='1'):
                c+=bi[kk]
        ee.append([c])
    e.append(ee)  
#kmap=[{b[x]:b[x] for x in range(len(b))} for y in range(len(b))]
kmap={b[i]:e[i] for i in range(len(e))}
for i,j in kmap.items():
    for g in range(len(j)):
            if(j[g][0] in f):
                j[g].append('*')
for i,j in kmap.items():
	print(i,j)




