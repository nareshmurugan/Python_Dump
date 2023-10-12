from collections import Counter as c
a=input()
d=c(a)
s='abcdefghijklmnopqrstuvwxyz'
w={y:x for x,y in enumerate(s,1)}
l=[]
for i in d:
    #print(d[i],i)
    for j in range(1,d[i]+1):
        s=i*j
    l.append(s)
    for k in range(len(s)):
        l.append(s[k:])
l=set(l)
wl=[]
for i in l:
    we=0
    for j in i:
        we+=w[j]
    wl.append(we)
for i in range(int(input())):
    if(int(input()) in wl):
        print("Yes")
    else:
        print("No")

