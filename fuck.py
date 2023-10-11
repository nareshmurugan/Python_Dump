a=int(input())
b=[]
for i in range(a):
    c=input().split()
    b.append(c)
l=[]
ll=[]
def query(x):
    global l,ll
    if(int(x) in l):
        ll.append('True')
    else:
        ll.append('False')
def add(y):
    global l,ll
    l.append(int(y))
def size():
    global l
    ll.append(len(l))
def remove(z):
    global l,ll
    if(int(z) in l):
        l.remove(int(z))
for j in b:
    if(j[0]=='query'):
        query(j[1])
    elif(j[0]=='add'):
        add(j[1])
    elif(j[0]=='size'):
        size()
    elif(j[0]=='remove'):
        remove(j[1])
for k in ll:
    print(k)
    
