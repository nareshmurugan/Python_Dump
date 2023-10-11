l=[]
a=int(input())
for i in range(a):
    b=input().split()
    l.append(b)  
ll=[]
def circle(r):
    global ll
    pi=3.141592653589793
    ll.append(float(pi*(r**2)))
def rectangle(l,b):
    global ll
    ll.append(float(l*b))
for j in l:
    if(j[0]=='circle'):
        circle(int(j[1]))
    elif(j[0]=='rectangle'):
        rectangle(int(j[1]),int(j[2]))
for k in ll:
    print('%1.2f'%k)
