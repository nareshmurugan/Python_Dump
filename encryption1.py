import math as m
#a=input()
a='ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'
a='chillout'
l=[]
r,c=m.ceil(m.sqrt(len(a))),m.floor(m.sqrt(len(a)))
o=0
p=[]
for i in range(r):
    print(a)
    l.append(a[:r])
    #print(a[:r])
    a=a[r:]
#print(l)
for v in l:
    print(len(v))
m=max(l,key=len)
for i in range(len(l)):
    if(len(l[i])!=len(m)):
        l[i]=l[i]+(' '*(len(m)-len(l[i])))
#print(l)    
for i in range(len(l)):
    co=''
    for j in range(len(l)):
        co+=l[j][i]
    p.append(co.rstrip())
print(*p)

    
