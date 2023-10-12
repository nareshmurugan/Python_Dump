def catmouse(a,b,c):
    if(abs(a-c)>abs(b-c)):
        print("Cat B")
    if(abs(a-c)<abs(b-c)):
        print("Cat A")
    if(abs(a-c)==abs(b-c)):
        print("Mouse C")
n=int(input())
l=[]
for i in range(n):
    x=list(map(int,input().split()))
    l.append(x)
for j in l:
    catmouse(j[0],j[1],j[2])
    
