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
def f1():
    #R1-->R1+|-R2=g1|g11
    g1=[int(R1[0])+int(R2[0]),int(R1[1])+int(R2[1]),int(R1[2])+int(R2[2])]
    g11=[int(R1[0])-int(R2[0]),int(R1[1])-int(R2[1]),int(R1[2])-int(R2[2])]
    #R2-->R2+|-R1=g2|g22
    g2=[int(R2[0])+int(R1[0]),int(R2[1])+int(R1[1]),int(R2[2])+int(R1[2])]
    g22=[int(R2[0])-int(R1[0]),int(R2[1])-int(R1[1]),int(R2[2])-int(R1[2])]
    #R3-->R3+|-R2=g3|g33
    g3=[int(R3[0])+int(R2[0]),int(R3[1])+int(R2[1]),int(R3[2])+int(R2[2])]
    g33=[int(R3[0])-int(R2[0]),int(R3[1])-int(R3[1]),int(R3[2])-int(R2[2])] 
    #R3-->R3+|-R1=g4|g44
    g4=[int(R3[0])+int(R1[0]),int(R3[1])+int(R1[1]),int(R3[2])+int(R1[2])]
    g44=[int(R3[0])-int(R1[0]),int(R3[1])-int(R1[1]),int(R3[2])-int(R1[2])]
    #R2-->R2+|-R3=g5|g55
    g5=[int(R2[0])+int(R3[0]),int(R2[1])+int(R3[1]),int(R2[2])+int(R3[2])]
    g55=[int(R1[0])-int(R3[0]),int(R2[1])-int(R3[1]),int(R2[2])-int(R3[2])]
    #R1-->R1+|-R3=g6|g66
    g6=[int(R1[0])+int(R3[0]),int(R1[1])+int(R3[1]),int(R1[2])+int(R3[2])]
    g66=[int(R1[0])-int(R3[0]),int(R1[1])-int(R3[1]),int(R1[2])-int(R3[2])]
    print(g1,g2,g3,g4,g5,g6)
f1()
 
    
 


    
