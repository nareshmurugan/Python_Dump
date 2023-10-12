import itertools as it
from itertools import combinations, chain
n=input()
s=list(map(int,input().split()))
ss=list(map(list, it.combinations(s,2)))
sss=[]
for i in ss:
    sss.append(abs(i[0]-i[1]))
print(min(sss))
