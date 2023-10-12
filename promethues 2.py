import numpy as n
X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
Z=int(input('ENTER THE COEFFECIENT OF Z1:\t'))
x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
z=int(input('ENTER THE COEFFECIENT OF Z2:\t'))
j=int(input('ENTER THE COEFFECIENT OF X3:\t'))
k=int(input('ENTER THE COEFFECIENT OF Y3:\t'))
l=int(input('ENTER THE COEFFECIENT OF Z3:\t'))
a=n.array([(X,Y,Z),(x,y,z),(j,k,l)])
print("THE GIVEN MATRIX\n",a)
A,B,C=a[0],a[1],a[2]
################################GROUP FIRST######################################
#R1<-->R2=t1<-->t2
a[0]=[x,y,z]
a[1]=[X,Y,Z]
#R2<-->R3=t2<-->t3
a[2]=[j,k,l]
a[1]=[x,y,z]
#R1<-->R3=t1<-->t3  
a[0]=[X,Y,Z]
a[2]=[j,k,l]
################################GROUP SECOND######################################
#R1-->R1+|-R2=g1|g11
g1=(A+B)
g11=[A-B]

#R2-->R2+|-R1=g2|g22
g2=[B+A]
g22=[B-A]

#R3-->R3+|-R2=g3|g33
g3=[C+B]
g33=[C-B]

#R3-->R3+|-R1=g4|g44
g4=[C+A]
g44=[C-A]

#R2-->R2+|-R3=g5|g55
g5=[B+C] 
g55=[B-C]

#R1-->R1+|-R3=g6|g66
g6=[A+C]
g66=[A-C]

################################GROUP THIRD######################################
#R2-->nR2+|-R1=g7|g77,n€R'n=R'
        
        
print(g1,g2,g3,g4,g5,g6,g11,g22,g33,g44,g55,g66)
