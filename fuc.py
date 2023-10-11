a=[0.8,0.5,0.5,0.2, 0.2, 0.1, 0.1]
b=0.4
for i in range(len(a)):
    if(p>=a[i]):
        a.insert(i,p)
        break
