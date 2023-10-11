noOp=int(input())
l=[]
ll=[]
for i in range(noOp):
    op,*Elem=input().split()
    ll.append([op,Elem])
for i in range(len(ll)):
    if ll[i][0]=='insert':
    	l.insert(int(ll[i][1][0]),int(ll[i][1][1]))
    elif ll[i][0]=='append':
    	l.append(int(ll[i][1][0]))
    elif ll[i][0]=='remove':
        l.remove(int(ll[i][1][0]))
    elif ll[i][0]=='print':
        print(l)
    elif ll[i][0]=='pop':
        l.pop()
    elif ll[i][0]=='sort':
        l.sort()
    elif ll[i][0]=='reverse':
        l.reverse()
