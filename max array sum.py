import itertools as it
n=int(input())
l=list(map(str,input().split()))
ll=[l[j:i] for i in range(n+1) for j in range(i) if len(l[j:i])>2]        
