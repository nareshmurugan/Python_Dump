X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
Z=int(input('ENTER THE COEFFECIENT OF Z1:\t'))
x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
z=int(input('ENTER THE COEFFECIENT OF Z2:\t'))
j=int(input('ENTER THE COEFFECIENT OF X3:\t'))
k=int(input('ENTER THE COEFFECIENT OF Y3:\t'))
l=int(input('ENTER THE COEFFECIENT OF Z3:\t'))
R1=[X,Y,Z]
R2=[x,y,z]
R3=[j,k,l]
################################GROUP SECOND######################################
#R1-->R1+|-R2=g1|g11
def G1(a,b,c,d,e,f):
    R1=[X,Y,Z]
    R2=[x,y,z]
    R3=[j,k,l]
    del R1
    R1=[X+x,Y+y,Z+z]
    print(R1)
def G11(a,b,c,d,e,f):
    R1=[X,Y,Z]
    R2=[x,y,z]
    R3=[j,k,l]
    del R1
    R1=[X-x,Y-y,Z-z]
    print(R1)
G11(x,y,z,X,Y,Z)
    

#R2-->R2+|-R1=g2|g22
def G2(a,b,c,d,e,f):
    g2=[x+X,y+Y,z+Z]
    print(g2)
G2(x,y,z,X,Y,Z)
def G22(a,b,c,d,e,f):
    g22=[x-X,y-Y,z-Z]
    print(g22)
G22(x,y,z,X,Y,Z)

#R3-->R3+|-R2=g3|g33
def G3(a,b,c,d,e,f):
    g3=[j+x,k+y,l+z]
    print(g3)
G3(x,y,z,j,k,l)
def G33(a,b,c,d,e,f):
    g33=[j-x,k-y,l-z]
    print(g33)
G33(x,y,z,j,k,l)

#R3-->R3+|-R1=g4|g44
def G4(a,b,c,d,e,f):
    g4=[j+X,k+Y,l+Z]
    print(g4)
G4(X,Y,Z,j,k,l)
def G44(a,b,c,d,e,f):
    g44=[j-X,k-Y,l-Z]
    print(g44)
G44(X,Y,Z,j,k,l)
#R2-->R2+|-R3=g5|g55
def G5(a,b,c,d,e,f):
    g5=[x+j,y+k,z+l]
    print(g5)
G5(x,y,z,j,k,l)
def G55(a,b,c,d,e,f):
    g55=[x-j,y-k,z-l]
    print(g55)
G55(x,y,z,j,k,l)
#R1-->R1+|-R3=g6|g66
def G6(a,b,c,d,e,f):
    g6=[X+j,Y+k,Z+l]
    print(g6)
G6(X,Y,Z,j,k,l)
def G66(a,b,c,d,e,f):
    g66=[X-j,Y-k,Z-l]
    print(g66)
G66(X,Y,Z,j,k,l)
def func:
    if(X=-int and x=int):
        G1(x,y,z,X,Y,Z)
        
    
    
