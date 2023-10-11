nc=int(input())
ns=input()
if(ns[0]=='D'):
    res=(ns.count('U')-ns.count('D'))+2   
else:
    res=(ns.count('U')-ns.count('D'))+1       
print(res)    
    
