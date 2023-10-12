ng=int(input())
a=int(input())
b=int(input())
l=[]
for m in range(b):
    c=list(input())
    l.append(c)
_u=[]
s=''
for _c in range(0,len(l[0])):
    for _j in range(b):
        _u.append(l[_j][_c])
        s+=str(l[_j][_c])
for o in l:
    o.sort()
my_list=_u
# How many elements each
# list should have
n = b
# using list comprehension
r=[my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
u=[]
_s=''
for c in range(0,len(l[0])):
    for j in range(b):
        u.append(l[j][c])
        _s+=str(l[j][c])            
my_list=u
# How many elements each
# list should have
n = b
# using list comprehension
_r=[my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
_h=''
for h in _r:
	h.sort()
	_h+=''.join(h)	
if(_s==_h):
    print('YES')
else:
    print('NO')
    
