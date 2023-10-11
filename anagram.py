#a=input()+" "
#b=input()
a="abcdefghijk"
b="abc"
l=len(b);s=0
an=[]
while 1:
    if(sorted(a[s:s+l])==sorted(b)):   
        an.append(s)
    s+=l
    if(len(a)==s+1 or len(a)==s-1):
        break
    print(s)
    
    
    
    
