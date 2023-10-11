X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
Z=int(input('ENTER THE COEFFECIENT OF Z1:\t'))
x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
z=int(input('ENTER THE COEFFECIENT OF Z2:\t'))
j=int(input('ENTER THE COEFFECIENT OF X3:\t'))
k=int(input('ENTER THE COEFFECIENT OF Y3:\t'))
l=int(input('ENTER THE COEFFECIENT OF Z3:\t'))
def display():
    print('\n',[X,Y,Z],'\n',[x,y,z],'\n',[j,k,l])
R1=[X,Y,Z]
R2=[x,y,z]
R3=[j,k,l]
################################GROUP FIRST######################################
#R1<-->R2=t1<-->t2
def t1():
    t1=[x,y,z]
    t2=[X,Y,Z]
#R2<-->R3=t2<-->t3
def t2():
    t3=[j,k,l]
    t4=[x,y,z]
#R1<-->R3=t1<-->t3
def t3():
    t5=[X,Y,Z]
    t6=[j,k,l]
################################GROUP SECOND######################################
#R1-->R1+|-R2=g1|g11
def G1(a,b,c,d,e,f):
    g1=[X+x,Y+y,Z+z]
    print(g1)
def G11(a,b,c,d,e,f):
    g11=[X-x,y-y,Z-z]
    print(g11)
#R2-->R2+|-R1=g2|g22
def G2(a,b,c,d,e,f):
    g2=[x+X,y+Y,z+Z]
    print(g2)
def G22(a,b,c,d,e,f):
    g22=[x-X,y-Y,z-Z]
    print(g22)
#R3-->R3+|-R2=g3|g33
def G3(a,b,c,d,e,f):
    g3=[j+x,k+y,l+z]
    print(g3)
def G33(a,b,c,d,e,f):
    g33=[j-x,k-y,l-z]
    print(g33)
#R3-->R3+|-R1=g4|g44
def G4(a,b,c,d,e,f):
    g4=[j+X,k+Y,l+Z]
    print(g4)
def G44(a,b,c,d,e,f):
    g44=[j-X,k-Y,l-Z]
    print(g44)
#R2-->R2+|-R3=g5|g55
def G5(a,b,c,d,e,f):
    g5=[x+j,y+k,z+l]
    print(g5)
def G55(a,b,c,d,e,f):
    g55=[x-j,y-k,z-l]
    print(g55)
#R1-->R1+|-R3=g6|g66
def G6(a,b,c,d,e,f):
    g6=[X+j,Y+k,Z+l]
    print(g6)
def G66(a,b,c,d,e,f):
    g66=[X-j,Y-k,Z-l]
    print(g66)
################################GROUP THIRD######################################
#R2-->nR2+|-R1=g7|g77,n€R'n=R'

def execute():
    G1(X,Y,Z,x,y,z)
    G2(X,Y,Z,x,y,z)
    G3(x,y,z,j,k,l)
    G4(X,Y,Z,j,k,l)
    G5(j,k,l,x,y,z)
    G6(X,Y,Z,j,k,l)
    G11(X,Y,Z,x,y,z)
    G22(X,Y,Z,x,y,z)
    G33(x,y,z,j,k,l)
    G44(X,Y,Z,j,k,l)
    G55(j,k,l,x,y,z)
    G66(X,Y,Z,j,k,l)
def optional():
    q=input("ENTER THE METHOD")
    if(q==G1):
        print(G1(X,Y,Z,x,y,z))
    elif(q==G2):
        G2(X,Y,Z,x,y,z)
    elif(q==G3):
        G3(x,y,z,j,k,l)
    elif(q==G4):
        G4(X,Y,Z,j,k,l)
    elif(q==G5):
        G5(j,k,l,x,y,z)
    elif(q==G6):
        G6(X,Y,Z,j,k,l)
    elif(q==G11):
        G11(X,Y,Z,x,y,z)
    elif(q==G22):
        G22(X,Y,Z,x,y,z)
    elif(q==G33):
        G33(x,y,z,j,k,l)
    elif(q==G44):
        G44(X,Y,Z,j,k,l)
    elif(q==G55):
        G55(j,k,l,x,y,z)
    elif(q==G66):
        G66(X,Y,Z,j,k,l)
display()        
execute()
optional()





        
