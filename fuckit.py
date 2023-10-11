l=[5,1,4,2,8]
s=False
while(not s):
    i=0
    while(l[i]>l[i+1]):
        l[i+1],l[i]=l[i],l[i+1]
        i=i+1
        s=True
        if(i==len(l)-2):
            break
        
