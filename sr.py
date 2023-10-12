import string as s
s=s.ascii_lowercase
b=input()
a=set(b)
l={i:b.count(i) for i in a}
for i in a:
    if(l[i]>1):
        b=b.replace(i*2,'')
    print(i)

