#l=input().split()
l=list(map(str,[110,112,200,311,422,666,777,776,456,445,66,53,88,88,76,232]))
ll=[]
for i in l:
    ll.append(i[0])
for j in sorted(set(ll)):
    print(f'{j} is  repeated {ll.count(j)} times')

