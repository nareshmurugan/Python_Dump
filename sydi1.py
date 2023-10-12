#synthetic division
print('''where coeff x**3 is always 1 and
s1 is coeff of x**2 and s2 is coeff x and d is constant''')
S1=int(input())
S2=int(input())
S3=int(input())
f=[]
for i in range(1,10):
    f.append(i)
    f.append(-i)
for j in f:
    l=[1,S1,S2,S3]
    lll=[1,0,0,0]
    ll=[0,0,0,0]
    for i in range(1,len(l)):
        ll[i]=(l[i-1]-ll[i-1])*j
        lll[i]=l[i]-ll[i]
    if(lll[-1]==0):
           break
#p=f.index(j)+1
#print(lll,f[p])
print(lll,-j)    

