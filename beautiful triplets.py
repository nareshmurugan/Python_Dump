import itertools as it
a=list(map(int,input().split()))[1]
b=list(map(int,input().split()))
l=0
for i in it.permutations(b,3):
    if((i[0]<i[1]<i[2]) and (i[1]-i[0]==i[2]-i[1]==a)):
        l+=1    
print(l)
