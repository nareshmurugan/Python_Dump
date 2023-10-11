#bubble sort
while(True):
    if(True not in ifl):
        break
    else:
        pass

    def f():
        ifl=[]
        for i in range(len(l)):
            if(i==len(l)-1):
                continue
            if(l[i]>l[i+1]):
                l[i+1],l[i]=l[i],l[i+1]
                swap=True
            else:
                swap=False
            ifl.append(swap)
            return ifl
f(l)            
l=[5,1,4,2,8]
