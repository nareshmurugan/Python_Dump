l=[[0.4, 0.2, 0.2, [0.1, 0], [0.1, 1]], [0.4, 0.2, [0.2, 0], [0.2, 1]], [0.4, [0.4, 0], [0.2, 1]], [[0.6, 0], [0.4, 1]]];p=[[0.4, 0.2, 0.2, 0.1, 0.1], [0.4, 0.2, 0.2, 0.2, 0], [0.4, 0.4, 0.2, 0, 0], [0.6, 0.4, 0, 0, 0]]
#l=[[0.8, 0.7, 0.5, 0.3, 0.2, [0.2, 0], [0.1, 1]], [0.8, 0.7, 0.5, 0.3, [0.3, 0], [0.2, 1]], [0.8, 0.7, 0.5, [0.5, 0], [0.3, 1]], [0.8, 0.8, [0.7, 0], [0.5, 1]], [1.2, [0.8, 0], [0.8, 1]], [[1.6, 0], [1.2, 1]]];p=[[0.8, 0.7, 0.5, 0.3, 0.2, 0.2, 0.1], [0.8, 0.7, 0.5, 0.3, 0.3, 0.2, 0], [0.8, 0.7, 0.5, 0.5, 0.3, 0, 0], [0.8, 0.8, 0.7, 0.5, 0, 0, 0], [1.2, 0.8, 0.8, 0, 0, 0, 0], [1.6, 1.2, 0, 0, 0, 0, 0]]
ff=p[0]
code=[]
for i in ff:
    co=''
    n=1
    c=[]
    for j in l:
        for k in j:
            if(len(j)==2):
                continue
            if(type(k)==list and (i in k)):
                co+=str(k[1])
                if(type(k)==list and k[1]!=1):
                    s=round(k[0]+j[j.index(k)+n][0],1);#print(s,k[0],j[j.index(k)+n][0]);
                    c.append(s)
                else:
                    pass
                #print(k,s)
                if(type(k)==list and (i in k) and k[1]!=1): 
                    o=l[l.index(j)+1:]
                print(o,i,k,j)
                #for g in l[l.index(j)+1:]:
                    #print(g,'*',l[l.index(j)+1:])
                    #print(g)
                    #for v in g:
                     #   print(v)
                                    
    print('\n')
    code.append(co)

                                
                
