lo=[[18, 1.4], [3, 1.0], [3, 1.0], [7, 0.4], [7, 0.4], [11, 0.2], [11, 0.2]]
#lo=[[18, 1.4], [7, 0.4], [7, 0.4], [18, 0.6], [18, 0.6], [18, 0.6], [18, 0.6]]
l=[[[0, 0.8], [1, 0.5], [2, 0.5], [3, 0.2], [4, 0.2], [5, 0.1, 0], [6, 0.1, 1]], [[0, 0.8], [1, 0.5], [2, 0.5], [11, 0.2], [3, 0.2, 0], [4, 0.2, 1]], [[0, 0.8], [1, 0.5], [2, 0.5], [7, 0.4, 0], [11, 0.2, 1]], [[0, 0.8], [18, 0.6], [1, 0.5, 0], [2, 0.5, 1]], [[3, 1.0], [0, 0.8, 0], [18, 0.6, 1]], [[18, 1.4, 0], [3, 1.0, 1]]]
p=[[[0, 0.8], [1, 0.5], [2, 0.5], [3, 0.2], [4, 0.2], [5, 0.1], [6, 0.1]], [[0, 0.8], [1, 0.5], [2, 0.5], [11, 0.2], [3, 0.2], [4, 0.2], 0], [[0, 0.8], [1, 0.5], [2, 0.5], [7, 0.4], [11, 0.2], 0, 0], [[0, 0.8], [18, 0.6], [1, 0.5], [2, 0.5], 0, 0, 0], [[3, 1.0], [0, 0.8], [18, 0.6], 0, 0, 0, 0], [[18, 1.4], [3, 1.0], 0, 0, 0, 0, 0]]
#ff=lo
ff=p[0]
code=[]
def fe(lo,l,co):
    u=[]
    ll=[]
    for i in lo:
        if(len(co)==2):
            continue
        co=''
        for ii in l:
            for j in ii:
                if(i == j[:2] and len(j)==3):
                    co+=str(j[2])
                    #print(co)
                    u.append(co)
                    if(type(j)==list and len(j)==3 and j[2]==1):
                        s=[j[0]+ii[ii.index(j)-n][0],round(j[1]+ii[ii.index(j)-n][1],1)]
                        ll.append(s)
                    elif(type(j)==list and len(j)==3):
                        s=[j[0]+ii[ii.index(j)+n][0],round(j[1]+ii[ii.index(j)+n][1],1)]
                        ll.append(s)
                    break
    lo=ll
    #print(u)
    return co,ll,u
for y in range(len(ff)):
    print(ff)
    for f in ff:
        c=[]
        n=1
        s=1
        for i in l:
            co=''
            for j in i:
                if(len(i)==2):
                    break
                if(type(j)==list and len(j)==3 and (f[0]==j[0])):
                    co+=str(j[2])
                    if(type(j)==list and len(j)==3 and j[2]==1):
                        s=[j[0]+i[i.index(j)-n][0],round(j[1]+i[i.index(j)-n][1],1)]
                        lo.append(s)
                    elif(type(j)==list and len(j)==3):
                        s=[j[0]+i[i.index(j)+n][0],round(j[1]+i[i.index(j)+n][1],1)]
                        lo.append(s)
                    co+=fe(lo,l,co)[0]
                    #print(fe(lo,l,co)[2])
                    c.append(co)
                    #if(lo
        #    print(f,j,s)
        #print('\n')
        code.append(c)
    #print(code)
    ff=lo
    #print(lo)
    break    








    
