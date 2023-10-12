import itertools as it
#n=input()
#s=input()
s='abaacdabd'
c=set(s)
l=[x for x in it.permutations(c)]
ll=[]
for i in l:
    for j in i:
        s.replace(j,'')
            
