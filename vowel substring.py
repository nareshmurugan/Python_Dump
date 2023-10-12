a=input()
b=int(input())
k=b
l=[]
m=0
n=0
s=['a','e','i','o','u']
while True:
    l.append(a[m:b])
    if(len(l[n])<k):
        break
    n+=1
    m+=1
    b+=1
ll=''
for i in l:
    for j in i:
        if(j in s):
            ll+='y'
        else:
            ll+='n'
if('y' not in ll):
    print("Not found!")
else:
    lll=[]
    nn=0
    mm=0
    kk=k
    while True:
        lll.append(ll[mm:k])
        if(len(l[nn])<kk):
            break
        nn+=1
        mm+=1
        k+=1
    c=[]
    for v in lll:
        c.append(v.count('y'))
    if('n' not in ll):
        print(l[0])    
    else:
        for q in c:
            if(q==max(c)):
                print(l[q])
                break
