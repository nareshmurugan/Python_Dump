import copy as c
b=input()
o=c.deepcopy(b)
a=set(b)
l=[]
for i in a:
    l.append([i,b.count(i)])
for j in l:
    if(j[1]>1):
        b=b.replace(j[0]*2,'')
        if(b!=o):
            bb=b[b.index(j[0]*2)+2]
            print(bb)
if(b==''):
    b='Empty String'
print(b)

