n=18
ll=[]
for i in range(1,n):
    l,k,m,n=str(i),str(oct(i))[2:],str(hex(i))[2:].upper(),str(bin(i))[2:]
    s1,s2,s3,s4=len(n)-len(str(l)),len(n)-len(str(k)),len(n)-len(str(m)),len(n)-len(str(n))
    print(" "*s1+l,(" "*s2)+k,(" "*s3)+m,(" "*s4)+n,sep=' ')
    
    
