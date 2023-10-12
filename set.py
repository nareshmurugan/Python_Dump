a=int(input())
b=set(list(input().split()))
no=int(input())
for i in range(no):
    o_=['intersection_update','update','symmetric_difference_update',
        'difference_update']
    _no=input().split()
    _o=set(list(input().split()))
    for i in range(len(_no)): 
        if(o_[i]=='intersection_update'):
            b=b.intersection_update(_o)
        elif(o_[i]=='update'):
            b=b.update(_o)
        elif(o_[i]=='symmetric_difference_update'):
            b=b.symmetric_difference_update(_o)
        elif(o_[i]=='difference_update'):
            b=b.difference_update(_o)
__a=[]
for i in b:
    __a.append(int(i))
print(sum(__a))    
    
