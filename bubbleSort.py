'''l=[5,1,4,2,8]
def fuck(l):
    i=0
    while(l[i]>l[i+1]):
        l[i+1],l[i]=l[i],l[i+1]
        i=i+1
        if(i==len(l)-2):
            break
    return l
'''
l=[5,1,4,2,8]
for i in range(100):
        while(l[i]>l[i+1]):
                l[i+1],l[i]=l[i],l[i+1]
                i=i+1
                if(i==len(l)-2):
                        break
                
    
