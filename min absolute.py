a=int(input())
b=input().split()
b=set(b)
b=list(b)
l=list(map(int,b))
ll=[]
lll=[]
for i in range(len(l)):
    for j in range(len(l)):
            if(l[i]==l[j]):
                continue
            ll.append([l[i],l[j]])                
for k in ll:
    lll.append(abs(k[0]-k[1]))
print(min(lll))
