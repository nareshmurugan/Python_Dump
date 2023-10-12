nFLAME=input().split()
noList,noModulo=int(nFLAME[0]),int(nFLAME[1])
tl=[]
for i in range(noList):
    listElements=input().split()[1:]
    lE=list(list(map(int,listElements)))
    tl.append(lE) 

mol=[]
for i in tl:
	for j in range(len(i)):
		i[j]=int(pow(i[j],2))
for _i in tl:
    mol.append(max(_i))
a=0
for _i in mol:
    a+=_i
print(a%noModulo)

