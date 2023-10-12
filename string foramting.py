'''ll,kl,ml,nl=[],[],[],[]
for i in range(1,18):
    a=[str(oct(i)),str(hex(i)),str(bin(i))]
    l,k,m,n=i,a[0][2:],a[1][2:].upper(),a[2][2:] 
    if i<10:
        ll.append(str(l).center(3,' '));kl.append("   {}".format(k.center(3,' ')));
        ml.append("   {}".format(m.center(3,' ')));
        nl.append("{}".format(n.center(3,' ')))
    else:
        print(l,k,m,n)
 
'''
ll,kl,ml,nl=[],[],[],[]
'''for i in range(20):
    if len(i)<2:
        ll.append(i)
        print(str(i).center(3,' '))		
    else:
        print(i)
'''

for i in range(1,18):
    a=[str(oct(i)),str(hex(i)),str(bin(i))]
    l,k,m,n=str(i),a[0][2:],a[1][2:].upper(),a[2][2:] 
    ll.append([l,k,m,n])
lll=[]
for i in range(len(ll)):
    lll.append(str(i))
    
    
