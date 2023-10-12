X=int(input('ENTER THE COEFFECIENT OF X1:\t'))
Y=int(input('ENTER THE COEFFECIENT OF Y1:\t'))
Z=int(input('ENTER THE COEFFECIENT OF Z1:\t'))
x=int(input('ENTER THE COEFFECIENT OF X2:\t'))
y=int(input('ENTER THE COEFFECIENT OF Y2:\t'))
z=int(input('ENTER THE COEFFECIENT OF Z2:\t'))
j=int(input('ENTER THE COEFFECIENT OF X3:\t'))
k=int(input('ENTER THE COEFFECIENT OF Y3:\t'))
l=int(input('ENTER THE COEFFECIENT OF Z3:\t'))
class row_echo:
    def __int__(self):
        R1=[X,Y,Z]
        R2=[x,y,z]
        R3=[j,k,l]
        n=int(input('ENTER THE NUMBER TO BE MULTIPLE IN ROW'))
        print('\n',[X,Y,Z],'\n',[x,y,z],'\n',[j,k,l])
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
    def G1():
        g1=[X+x,Y+y,Z+z]
        g11=[X-x,y-y,Z-z]

#R2-->R2+|-R1=g2|g22
    def G2():
        g2=[x+X,y+Y,z+Z]
        g22=[x-X,y-Y,z-Z]

#R3-->R3+|-R2=g3|g33
    def G3():
        g3=[j+x,k+y,l+z]
        g33=[j-x,k-y,l-z]

#R3-->R3+|-R1=g4|g44
    def G4():
        g4=[j+X,k+Y,l+Z]
        g44=[j-X,k-Y,l-Z]

#R2-->R2+|-R3=g5|g55
    def G5():
        g5=[x+j,y+k,z+l]
        g55=[x-j,y-k,z-l]

#R1-->R1+|-R3=g6|g66
    def G6():
        g6=[X+j,Y+k,Z+l]
        g66=[X-j,Y-k,Z-l]

################################GROUP THIRD######################################
#R2-->nR2+|-R1=g7|g77,n€R'n=R'
    def G7():
        g7=[n*(x)+X,n*(y)+Y,n*(z)+Z]
        g77=[n*(x)-X,n*(y)-Y,n*(z)-Z]
#R3-->nR3+|-R2=g8|g88,n€R'n=R'
    def G8():
        g8=[n*(j)+x,n*(k)+(y),n*(l)+(z)]
        g88=[n*(j)-x,n*(k)-(y),n*(l)-(z)]
#R3-->nR3+|-R1=g7|g77,n€R'n=R'
    def G9():       
        g9=[n*(j)+X,n*(k)+(Y),n*(l)+(Z)]
        g99=[n*(j)-X,n*(k)-(Y),n*(l)-(Z)]
    def execute(self):
        self.G1()
        self.G2()
        self.G3()
        self.G4()
        self.G5()
        self.G6()
        self.G7()
        self.G8()
        self.G9()
    def display(self):
        print(g1,g2,g3,g4,g5,g6,g11,g22,g33,g44,g55,g66,g7,g77,g8,g88,g9,g99)
r=row_echo()
r.execute()
r.display()





        
