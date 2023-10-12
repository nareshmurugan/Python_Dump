a=input()
b=set(map(int,input().split()))
c=int(input())
l=[]
for i in range(c):
    d=input().split()
    l.append(d)
def pop():
    b.pop()
def remove(w):
    global b
    b.remove(w)
def discard(e):
    global b
    b.discard(e)
for j in l:
    if(j[0]=='pop'):
        pop()
    elif(j[0]=='remove'):
        remove(int(j[1]))
    elif(j[0]=='discard'):
        discard(int(j[1]))
print(sum(b))
        
    
