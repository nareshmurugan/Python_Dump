from collections import OrderedDict
a=input()
n=int(input())
r=[a[i * n:(i + 1) * n] for i in range((len(a) + n - 1) // n )]
_r=[]
for j in r:
    _ll= OrderedDict.fromkeys(j,1)
    _r.append(_ll)
_res=[]
for k in _r:
    _res.append(list(k))

for m in _res:
    print(''.join(m))



