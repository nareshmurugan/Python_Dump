a=[6,4,1,2,5,6,4,8,6,7,6,9]
l=[]
lll=[]
for i in a:
    l.append([i,a.count(i)])
ll=dict(l)    
for j in ll:
    lll.extend([j]*ll[j])
print(lll)
