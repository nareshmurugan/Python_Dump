X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
Z=int(input('ENTER THE COEFFECIENT OF Z1:\t'))
x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
z=int(input('ENTER THE COEFFECIENT OF Z2:\t'))
j=int(input('ENTER THE COEFFECIENT OF X3:\t'))
k=int(input('ENTER THE COEFFECIENT OF Y3:\t'))
l=int(input('ENTER THE COEFFECIENT OF Z3:\t'))
print('\n',[X,Y,Z],'\n',[x,y,z],'\n',[j,k,l])
#R1+R2
def G1(a,b,c,d,e,f):
    R1=[X,Y,Z]
    R2=[x,y,z]
    del R1
    R3=[j,k,l]
    R1=[X+x,Y+y,Z+z]
    print(R1)
G1(x,y,z,X,Y,Z)
#R1-R2
def G2(a,b,c,d,e,f):
    R1=[X,Y,Z]
    R2=[x,y,z]
    del R1
    R3=[j,k,l]
    R1=[X-x,Y-y,Z-z]
    print(R1)
G2(x,y,z,X,Y,Z)
#nR1-R2
def gn11(a,b,c,d,e,f):
    global x
    if(X==1):
        x=x
        R1=[x*X,x*Y,x*Z]
        R1[0]=X
        R1[1]=Y
        R1[2]=Z
        R1=[X-x,Y-y,Z-z]
        print(R1)
gn11(x,y,z,X,Y,Z)    
#####################################
def gn21(a,b,c,d,e,f):
        R1=[x*X,x*Y,x*Z]
        R1[0]=X
        R1[1]=Y
        R1[2]=Z
        R1=[X-x,Y-y,Z-z]
        print(R1)
gn21(x,y,z,X,Y,Z)
