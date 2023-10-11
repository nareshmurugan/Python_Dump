import string as s
ss=s.ascii_lowercase
vo=['a','e','i','o','u']
def ecodeString(s,n):
    es=''
    for jj in s:
        if jj in vo:
            es+=ss[ss.index(jj)+1]
        elif jj not in vo:
            if(jj==ss[-1]):
                es+=ss[0]
            else:
                es+=ss[ss.index(jj)-1]
    return es
a=int(input())
l=[]
for i in range(a):
    aa=int(input())
    aaa=input()
    l.append([aa,aaa])    
for j in l:
    print(ecodeString(j[1],j[0]))
    
