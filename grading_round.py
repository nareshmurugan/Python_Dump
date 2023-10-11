l=[]
g=[x for x in range(0,101,5)]
a=int(input())
for i in range(a):
    b=int(input())
    l.append(b)
for j in l:
    if(j<38):
        print(j)        
    else:
        if(j+1 in g):
            print(j+1)
        elif(j+2 in g):
            print(j+2)
        else:
            print(j)
