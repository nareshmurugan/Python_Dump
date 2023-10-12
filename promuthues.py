class row():
    import numpy as n
    L=list(input("ENTER THE FIRST ROW"))
    M=list(input("ENTER THE FIRST ROW"))
    N=list(input("ENTER THE FIRST ROW"))
    X,Y,Z,x,y,z,j,k,l=int(L[0]),int(L[1]),int(L[2]),int(M[0]),int(M[1]),int(M[2]),int(N[0]),int(N[1]),int(N[2])
    a=n.array([(X,Y,Z),(x,y,z),(j,k,l)])
    print("THE GIVEN MATRIX\n",a)
    A,B,C=a[0],a[1],a[2]
################################GROUP FIRST######################################
#R1<-->R2=t1<-->t2
    def t1(self):
        a[0]=[x,y,z]
        a[1]=[X,Y,Z]
#R2<-->R3=t2<-->t3
    def t2(self):
        a[2]=[j,k,l]
        a[1]=[x,y,z]
#R1<-->R3=t1<-->t3
    def t3(self):
        a[0]=[X,Y,Z]
        a[2]=[j,k,l]
################################GROUP SECOND######################################
#R1-->R1+|-R2=g1|g11
    def G1(self):
        g1=(A+B)
    def G11(self):
        g11=[A-B]

#R2-->R2+|-R1=g2|g22
    def G2(self):
        g2=[B+A]
    def G22(self):
        g22=[B-A]

#R3-->R3+|-R2=g3|g33
    def G3(self):
        g3=[C+B]
    def G33(self):
        g33=[C-B]

#R3-->R3+|-R1=g4|g44
    def G4(self):
        g4=[C+A]
    def G44(self):
        g44=[C-A]

#R2-->R2+|-R3=g5|g55
    def G5(self):       
        g5=[B+C]
    def G55(self):
        g55=[B-c]

#R1-->R1+|-R3=g6|g66
    def G6(self):
        g6=[A+C]
    def G66(self):
        g66=[A-C]

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






















        
