l=[110,112,200,311,422,666,777,776,456,445,66,53,88,88,76,232]
ll=[]
for i in l:
    if(len(str(i))==1):
        ll.append(int(i))
        continue
    for j in range(len(str(i))-1):
        i=i/10
    ll.append(int(i))
for k in sorted(set(ll)):
    print(f'{k} is  repeated {ll.count(k)} times')
