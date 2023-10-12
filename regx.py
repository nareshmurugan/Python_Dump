a=int(input())
l=[]
for i in range(a):
    n=input()
    if(n[-10:]=="@gmail.com"):
        l.append(n)
    else:
        None
ll=[]
for j in range(len(l)):
	ll.append(l[j].split()[0])
ll=sorted(ll)
for k in ll:
    print(k)
    
    
