n=int(input())
m=[]
for i in range(n):
    l=input().split()
    l=list(map(int,l))
    m.append(l)
x1=0
x2=0
p=0
q=n-1
for j in m:
    x1+=j[p]
    p+=1
for j in m:
    x2+=j[q]
    q-=1
print(abs(x1-x2))
        
