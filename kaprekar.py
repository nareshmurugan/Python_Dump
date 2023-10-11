l=[1,]
for i in range(10000):
    le=len(str(i))
    if(len(str(i**2))!=1):
        #print(int(str(i**2)[:-le]),int(str(i**2)[-le:]))
        if((int(str(i**2)[:-le])+int(str(i**2)[-le:]))==i):
            l.append(i)
        elif((int(str(i**2)[:-le ])+int(str(i**2)[-le:]))==i):
            l.append(i)
