l=[[0.4, 0.2, 0.2, [0.1, 0], [0.1, 1]], [0.4, 0.2, [0.2, 0], [0.2, 1]], [0.4, [0.4, 0], [0.2, 1]], [[0.6, 0], [0.4, 1]]]
p=[[0.4, 0.2, 0.2, 0.1, 0.1], [0.4, 0.2, 0.2, 0.2, 0], [0.4, 0.4, 0.2, 0, 0], [0.6, 0.4, 0, 0, 0]]
code=[]
ff=p[0]
for i in ff:
    co=''
    for j in l:
        for k in j:
            if(type(k)==list and (i in k)):
                print(k,(i,k),type(k)==list and (i in k))
                co+=str(k[1])
                print('fuck')
                s=j.index(k)+1
                if(s==2):
                    continue
                n=round(k[0]+j[s][0],1)            
                for h in l[l.index(j)+1]:
                    if(type(h)==list and (n in h)):
                        print(h,(n,h),type(h)==list and (n in h))
                        co+=str(h[1])
                        print('fuck')
                        
        code.append(co)

                
