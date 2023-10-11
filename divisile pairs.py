import itertools as it
b=list(map(int,input().split()))[1]
a=list(map(int,input().split()))
l=0
for i in it.permutations(a,2):
    if(i[0]<i[1] and (i[0]+i[1])%b==0):
        l=l+1
    else:
        pass
print(l)
