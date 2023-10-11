'''
HUFFMAN CODING
'''
import copy as c
#a=list(map(float,input().split()))
a=[0.8, 0.7, 0.5, 0.3, 0.2, 0.2, 0.1]
a=sorted(a,reverse=True)
l=[a]
d=[]
for i in a:
    p=round(a[-1]+a[-2],1)
    s=a+[p]
    a=sorted(s,reverse=True)
    l.append(a)
    del a[-2:]
    if len(a)==2 :
        break
p=c.deepcopy(l)
for _,j in enumerate(l):
    j[-2:]=[[j[-2],0],[j[-1],1]]
    d.append(l)
    if len(l)==2:
        break
for k in l:
    print(k[:])
#log
#round(Pi*math.log(1/Pi,2),5)
