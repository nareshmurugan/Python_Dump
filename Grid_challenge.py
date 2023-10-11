a=int(input())
b=int(input())
l=[]
for m in range(b):
    c=list(input())
    l.append(c)
dic={i:chr(i) for i in range(97,123)}
ll=[]
j=[h for h in range(b)]
for f in l:
    k=[]
    for o in j:
        k.append(f[o])
        ll.append(k)
b=[]
for i in ll:
    b.append(tuple(i))
b=set(b)
g=[]
for i in b:
    g.append(list(i))
#ll is the row
#g is the column 
'''c1='yes'
c2='no'
s=[]
d=[]
for ss in ll:
    s.append(ss)
    ss.sort()
for dd in g:
    d.append(dd)
    dd.sort()
#for u in range(b):
    
'''
