a=int(input())
l=[input() for i in range(a)]
ll=[]
for s in l:
    b=0
    for i in range(len(s)-1):
        if (s[i]==s[i+1]):
            b+=1
    ll.append(b)
for r in ll:
    print(r)
    
