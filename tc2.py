import itertools as it
n=input()
a=input()
s=set(a)
l=[i for i in it.permutations(s,2)]
ll=set(a.replace(i[0],'').replace(i[1],'') for i in l)
lll=[]
for j in ll:    
    if(len(j)%2!=0):
        ls=j[:len(j)//2+1]
        rs=j[(len(j)//2):][::-1]
    else:
        ls=j[:len(j)//2]
        rs=j[(len(j)//2):][::-1]
    if(ls==rs or ls[::-1]==rs):
        lll.append(j)
print(len(max(lll,key=lambda x:len(x))))
