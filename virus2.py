bs=input()
np=int(input())
l=[]
for i in range(np):
    a=input()
    l.append(a)
def fuck():
    b=''
    ll=[]
    for i in range(len(l)):
        for j in l[i]:
            print([j][i],bs,[j][i] in bs)
            if([j][i] in bs):
                aa='s'
                b+=aa
            else:
                aa='n'
                b+=aa
            if(l[i]==l[-1]):
                ll.append(b)
        break

for p in l:
    fuck()
    
