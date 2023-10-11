'''
HUFFMAN CODING
'''
import copy as c
#a=list(map(float,input().split()))
a=[0.4,0.2, 0.2, 0.1, 0.1]
#a=[0.8,0.5,0.5,0.2, 0.2, 0.1, 0.1]
a=sorted(a,reverse=True)
a=[[t,tt] for t,tt in enumerate(a)]
l=[c.deepcopy(a)]
for i in range(len(a)):
    p=round(a[-1][1]+a[-2][1],1);_p=a[-1][0]+a[-2][0]
    for y in range(len(a)):
        if(p>=a[y][1]):
            a.insert(y,[_p,p])
            print(y,p,a[y][1])
            break
    #ss=lambda a:a[1]
    #a=sorted(a,key=ss,reverse=True)
    del a[-2:]
    l.append(c.deepcopy(a))
    print(a)
    if len(a)==2 :
        break
pp=c.deepcopy(l)
for j in range(len(l)):
    l[j][-2:]=[[l[j][-2][0],l[j][-2][1],0],[l[j][-1][0],l[j][-1][1],1]]
    if len(l)==2:
        break
for k in l:
    print(k)
print('\n')
d=c.deepcopy(l)
dd=c.deepcopy(pp)
_=[0]
le=len(l)+1
for g in range(len(l)):
    l[g].extend((le-len(l[g]))*_)
    pp[g].extend((le-len(pp[g]))*_)
for _i in range(len(l)+1):
	for _j in range(len(l)):
		print(l[_j][_i],end='   ')
	print('\n')    
for __i in range(len(pp)+1):
	for __j in range(len(l)):
		print(pp[__j][__i],end='   ')
	print('\n')














#log
#round(Pi*math.log(1/Pi,2),5)
