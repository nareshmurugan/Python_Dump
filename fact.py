'''def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact (n-1)
print (fact (0))
print (fact (5))
'''
l=[5,1,4,2,8]
def fuck(l):
    s=0
    if s:
        return 1
    else:
        i=0
        while(l[i]>l[i+1]):
            l[i+1],l[i]=l[i],l[i+1]
            i=i+1
            s=1     
            if(i==len(l)-2):
                break
    return l
print(fuck(l))
