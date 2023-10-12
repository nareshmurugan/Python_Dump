def fuck(x):
    s=[l for l in range(1,1000)]
    nn=2
    for o in a:
        for i in s:
            for j in range(nn,o+1):
                print(i,j,i&j)
            nn+=1
        o-=1
        if(o==o):
            break
    return i,j, i&j
