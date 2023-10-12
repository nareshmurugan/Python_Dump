import random
a=int(input())
b=input().split()
b=list(map(int,b))
l=[[]]
ll=[]
for j in range(len(b)):
    random.shuffle(b)
    l[j].append((2**j)*b[j])
    l.append([])
