'''
HUFFMAN CODING
'''
import copy as c
#a=list(map(float,input().split()))
#a=[0.8,0.5,0.5,0.2, 0.2, 0.1, 0.1]
a=[0.4,0.2,0.2,0.1,0.1]
a=sorted(a,reverse=True)
l=[c.deepcopy(a)]
d=[]
for i in range(len(a)):
    p=round(a[-1]+a[-2],1)
    s=a+[p]
    a=sorted(s,reverse=True)
    l.append(a)
    del a[-2:]
    if len(a)==2 :
        break
p=c.deepcopy(l)
for j in range(len(l)):
    l[j][-2:]=[[l[j][-2],0],[l[j][-1],1]]
    d.append(l)
    if len(l)==2:
        break
for k in l:
    print(k)
print('\n')
_=[0]
le=len(l)+1
for g in range(len(l)):
    l[g].extend((le-len(l[g]))*_)
    p[g].extend((le-len(p[g]))*_)
for _i in range(len(l)+1):
	for _j in range(len(l)):
		print(l[_j][_i],end='   ')
	print('\n')    
for __i in range(len(p)+1):
	for __j in range(len(l)):
		print(p[__j][__i],end='   ')
	print('\n')
















#log
#round(Pi*math.log(1/Pi,2),5)
