a=int(input())
b=[set(input()) for i in range(a)]
k=[]
_a=0
for i in range(len(b)):
    if(len(b)==i+1):
        break
    k.append(b[i+1]&b[i]);_k=b[i+1]&b[i]
    k.append(k[_a]&_k)
    _a+=1
print(len(k[-1]))
