n=18

for i in range(1,n):
    a=[str(oct(i)),str(hex(i)),str(bin(i))]
    l,k,m,n=str(i),a[0][2:],a[1][2:].upper(),a[2][2:] 
    ll.append(a)
for i in range(len(ll)):
    s1,s2,s3,s4=len(l)-len(str(n)),len(k)-len(str(n)),len(m)-len(str(n)),len(n)-len(str(n))
    print(" "*s1+l,(" "*s2)+k,(" "*s3)+m,(" "*s4)+n,sep=' ')
    
    
