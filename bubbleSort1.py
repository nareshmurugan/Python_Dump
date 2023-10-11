#bubble
import time
start=time.time()
l=[81,94,11,96,12,35,17,95,28,58]
print(f'The given list is {l}')
swap=True
while 1:
    ll=[]
    for i in range(len(l)-1):
        if(l[i]>l[i+1]):
            l[i+1],l[i]=l[i],l[i+1]
            s=0
            ll.append(s)
        else:
            s=1
            ll.append(s)
    if(all(ll)):
        break
end=time.time()
print(f'The bubble sorted list: {l}')    
print(end-start)
