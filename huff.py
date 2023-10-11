l=[[0.4, 0.2, 0.2, [0.1, 0], [0.1, 1]], [0.4, 0.2, [0.2, 0], [0.2, 1]], [0.4, [0.4, 0], [0.2, 1]], [[0.6, 0], [0.4, 1]]]
p=[[0.4, 0.2, 0.2, 0.1, 0.1], [0.4, 0.2, 0.2, 0.2, 0], [0.4, 0.4, 0.2, 0, 0], [0.6, 0.4, 0, 0, 0]]
code=[]
ff=p[0]
for i in ff:
    co=''
    for j in l:
        for k in j:
            print(k,(i,k),type(k)==list and (i in k))
            if(type(k)==list and (i in k)):
                co+=str(k[1])
                
    code.append(co)
    #elif(f is list and f==f[0]):
                
