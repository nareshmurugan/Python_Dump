import numpy as n
#x,Y=int(input("ENTER THE NUMBER OF ROWS")),int(input("ENTER THE NUMBER OF COLUMNS"))
#USING SPLIT FUNCTION WE GET INPUT AS SPACE SPERATED STRING  
a,b,c=str(input("ENTER THE FIRST ROW IN SERIOUS:")),str(input("ENTER THE SECOND ROW IN SERIOUS:")),str(input("ENTER THE THIRD ROW IN SERIOUS"))
print(a,b,c,end='\n')
d,e,f=a.split(),b.split(),c.split()#ASIGNING THE STRING AS ELEMENTS
l=(int(d[0]),int(d[1]),int(d[2]))#R1

k=(int(e[0]),int(e[1]),int(e[2]))#R2
m=(int(f[0]),int(f[1]),int(f[2]))#R3
g=n.array([l,k,m])#MATRIX(R1,R2,R3)
print("THIS IS THE GIVEN ARRRAY\n",g)
r1,r2,r3=g[0],g[1],g[2]
if(l[0]!=1):#TRYING TO CHANGING ROWS FOR THE ELEMENT 1 ON FRIST
    if(k[0]==1 or k[0]==-1):
        g=n.array([k,l,m])
    elif(m[0]==1 or m[0]==-1):
        g=n.array([m,k,l])
        print(g,'\n')
    if(g[0,0]==g[1,0]):#DIVIDING R1 AND R2 FOR GETTING ONE AS FIRST ELEMENT
        g[0]=g[1]/g[0]
        print(g,'\n')
    elif(g[1,0]==g[2,0]):
        g[0]=g[2]/g[1]
    elif(g[0,0]==g[2,0]):
        g[0]=g[0]/g[2]
if(g[0,0]==-1):
    g[0]=g[0]*-1
elif(g[1,0]==-1):
    g[1]=g[1]*-1
elif(g[2,0]==-1):
    g[2]=g[2]*-1
#USING FOR LOOP WE GET THE 1 BY SUBRACTING ANOTHER ROW 
print(g)
if(g[0,0]!=1 and g[1,0]!=1 and g[2,0]!=1):
#USING FOR LOOP WE GET THE 1 BY SUBRACTING ANOTHER ROW 
    for i in range(1,1000):
        if((i*g[0,0])-g[1,0]==1):#TRYING TO CONNECT R1 AND R2 AND GET 1 BY ADDING
            rC11=i*g[0]-g[1]
            g[0]=rC11
            print(g,i)
        elif((i*g[0,0])+g[1,0]==1):#TRYING TO CONNECT R1 AND R2 AND GET 1 BY SUBRACTING
            rC11=i*g[0]+g[1]
            g[0]=rC11
            print(g,i)
        elif((i*g[0,0])+g[2,0]==1):#TRYING TO CONNECT R1 AND R3 AND GET 1 BY ADDING
            rC11=i*g[0]+g[1]
            g[0]=rC11
            print(g,i)
        elif(i*g[0,0]-g[2,0]==1):#TRYING TO CONNECT R1 AND R3 AND GET 1 BY SUBRACTING
            rC11=i*g[0]-g[1]
            g[0]=rC11
            print(g,i)
        elif(i*g[1,0]-g[2,0]==1):#TRYING TO CONNECT R2 AND R3 AND GET 1 BY SUBRACTING
            rC11=i*g[0]-g[1]
            g[0]=rC11
            print(g,i)
        elif(i*g[1,0]+g[2,0]==1):#TRYING TO CONNECT R2 AND R3 AND GET 1 BY ADDING
            rC11=i*g[0]+g[1]
            g[0]=rC11
            print(g,i)
            i+=1
#AFTER THIS ALL WAY WE WON GET ONE MEANS WE DO FRIST ROW FRIST ELEMENT MUTIPLY TO THE
#-SECOND ROW FULLY AND SECOND FIRST ELEMENT MUTIPLY TO FIRST ROW AND DIVIDE ROW 1 AND ROW 2
else:
    rc1=g[0,0]*r2/g[1,0]*r1
    g[0]=rc1
print(g)
