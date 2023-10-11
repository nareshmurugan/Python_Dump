o_=['intersection_update','update','symmetric_difference_update',
        'difference_update']
nel=set([1,2,3,4,5])
nelemen=[33,44,55,66]
for n in range(len(o_)):
        nel=set([1,2,3,4,5])
        if(o_[n]=='intersection_update'):
            nel.intersection_update(nelemen)
        elif(o_[n]=='update'):
            nel.update(nelemen)
        elif(o_[n]=='symmetric_difference_update'):
            nel.symmetric_difference_update(nelemen)
        elif(o_[n]=='difference_update'):
            nel.difference_update(nelemen)
        print(nel)
