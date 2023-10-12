def print_formatted(n):
    ll,kl,ml,nl=1,1,1,1
    for i in range(1,n+1):
        a=[str(oct(i)),str(hex(i)),str(bin(i))]
        l,k,m,n=i,a[0][2:],a[1][2:].upper(),a[2][2:]
        if(len(str(l))>2):
            ll+=2
        print(str(l).center(ll,' '),k,m,n)
print_formatted(17)
    
