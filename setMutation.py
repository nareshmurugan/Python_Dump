a=input()
b=set(map(int,input().split()))
c=int(input())
l=[]
for i in range(c):
    d=input().split()
    e=set(map(int,input().split()))
    l.append([d[0],e])
def intersection_update(q):
    b.intersection_update(q)
def difference_update(w):
    b.difference_update(w)
def symmetric_difference_update(e):
    b.symmetric_difference_update(e)
def update(t):
    b.update(t)
for j in l:
    if(j[0]=='intersection_update'):
        intersection_update(j[1])
    elif(j[0]=='difference_update'):
        difference_update(j[1])
    elif(j[0]=='symmetric_difference_update'):
        symmetric_difference_update(j[1])
    elif(j[0]=='update'):
        update(j[1])
print(sum(b))
        
    
