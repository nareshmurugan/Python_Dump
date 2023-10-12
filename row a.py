X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
Z=int(input('ENTER THE COEFFECIENT OF Z1:\t'))
x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
z=int(input('ENTER THE COEFFECIENT OF Z2:\t'))
j=int(input('ENTER THE COEFFECIENT OF X3:\t'))
k=int(input('ENTER THE COEFFECIENT OF Y3:\t'))
l=int(input('ENTER THE COEFFECIENT OF Z3:\t'))
class row:
    
    def __int__(self):
        R1=[X,Y,Z]
        R2=[x,y,z]
        R3=[j,k,l]
################################GROUP FIRST######################################
#R1<-->R2=t1<-->t2
    def t1(self):
        t1=[x,y,z]
        t2=[X,Y,Z]
#R2<-->R3=t2<-->t3
    def t2(self):
        t3=[j,k,l]
        t4=[x,y,z]
#R1<-->R3=t1<-->t3
    def t3(self):
        t5=[X,Y,Z]
        t6=[j,k,l]
################################GROUP SECOND######################################
#R1-->R1+|-R2=g1|g11
    def G1(self):
        g1=[X+x,Y+y,Z+z]
    def G11(self):
        g11=[X-x,y-y,Z-z]

#R2-->R2+|-R1=g2|g22
    def G2(self):
        g2=[x+X,y+Y,z+Z]
    def G22(self):
        g22=[x-X,y-Y,z-Z]

#R3-->R3+|-R2=g3|g33
    def G3(self):
        g3=[j+x,k+y,l+z]
    def G33(self):
        g33=[j-x,k-y,l-z]

#R3-->R3+|-R1=g4|g44
    def G4(self):
        g4=[j+X,k+Y,l+Z]
    def G44(self):
        g44=[j-X,k-Y,l-Z]

#R2-->R2+|-R3=g5|g55
    def G5(self):
        g5=[x+j,y+k,z+l]
    def G55(self):
        g55=[x-j,y-k,z-l]

#R1-->R1+|-R3=g6|g66
    def G6(self):
        g6=[X+j,Y+k,Z+l]
    def G66(self):
        g66=[X-j,Y-k,Z-l]

################################GROUP THIRD######################################
#R2-->nR2+|-R1=g7|g77,n€R'n=R'
    
    def execute(self):
        self.G1()
        self.G2()
        self.G3()
        self.G4()
        self.G5()
        self.G6()
        self.G11()
        self.G22()
        self.G33()
        self.G44()
        self.G55()
        self.G66()
    def display(self):
        print('\n',[X,Y,Z],'\n',[x,y,z],'\n',[j,k,l])
        
r=row()
r.execute()
r.display()





        
