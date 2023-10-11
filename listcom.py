a=int(input())
b=int(input())
c=int(input())
n=int(input())
l=[]
ll=[]
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            l.append([i,j,k])
for y in l:
    if(sum(y)!=n):
        ll.append(y)
print(ll)
