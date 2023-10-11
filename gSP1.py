l=[110,112,200,311,422,666,777,776,456,445,66,53,88,88,76,232]
ll=[]
def intlen(n):
    c=0
    while(int(n)!=0):
        n=n/10
        c+=1
    return c
for i in l:
    for j in range(intlen(i)-1):
        i=i/10
        print(i)
    ll.append(int(i))
    print('\n')
for k in sorted(set(ll)):
    print(f'{k} is  repeated {ll.count(k)} times')
