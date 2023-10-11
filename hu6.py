l=[[[0, 0.8], [1, 0.5], [2, 0.5], [3, 0.2], [4, 0.2], [5, 0.1, 0], [6, 0.1, 1]], [[0, 0.8], [1, 0.5], [2, 0.5], [11, 0.2], [3, 0.2, 0], [4, 0.2, 1]], [[0, 0.8], [1, 0.5], [2, 0.5], [7, 0.4, 0], [11, 0.2, 1]], [[0, 0.8], [18, 0.6], [1, 0.5, 0], [2, 0.5, 1]], [[3, 1.0], [0, 0.8, 0], [18, 0.6, 1]], [[18, 1.4, 0], [3, 1.0, 1]]]
p=[[[0, 0.8], [1, 0.5], [2, 0.5], [3, 0.2], [4, 0.2], [5, 0.1], [6, 0.1]], [[0, 0.8], [1, 0.5], [2, 0.5], [11, 0.2], [3, 0.2], [4, 0.2], 0], [[0, 0.8], [1, 0.5], [2, 0.5], [7, 0.4], [11, 0.2], 0, 0], [[0, 0.8], [18, 0.6], [1, 0.5], [2, 0.5], 0, 0, 0], [[3, 1.0], [0, 0.8], [18, 0.6], 0, 0, 0, 0], [[18, 1.4], [3, 1.0], 0, 0, 0, 0, 0]]
ff=p[0]
code=[]
lo=[]
def fe():
    for i in lo:
        co=''
        for ii in l:
            for j in ii:
                if(i == j[:2] and len(j)==3):
                    co+=str(j[2])
                    break
    return co
while True:
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
                        co+=fe()
                    c.append(co)
               #print(f,j,s)
        code.append(c)
    print('\n')
    ff=lo
    if(len(lo)==2):
        break
    
python=[]
python.append(co)                 














'''









            if(len(j)==2):
                continue
            if(type(k[0])==list and (i in k)):
                co+=str(k[1])
                if(type(k)==list and k[1]!=1):
                    s=round(k[0][1]+j[j.index(k)+n][0][1],1)
'''
