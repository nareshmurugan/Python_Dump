import sympy as s
import numpy as n
import math
#x,Y=int(input("ENTER THE NUMBER OF ROWS")),int(input("ENTER THE NUMBER OF COLUMNS"))
#USING SPLIT FUNCTION WE GET INPUT AS SPACE SPERATED STRING  
a,b,c=str(input()),str(input()),str(input())
print(a,b,c,end='\n')
d,e,f=a.split(),b.split(),c.split()#ASIGNING THE STRING AS ELEMENTS
l=(int(d[0]),int(d[1]),int(d[2]))#R1
k=(int(e[0]),int(e[1]),int(e[2]))#R2
m=(int(f[0]),int(f[1]),int(f[2]))#R3
arr=n.array([l,k,m])#MATRIX(R1,R2,R3)
print("THIS IS THE GIVEN ARRRAY\n",arr)
###############################################################################################
S1=sum(arr.diagonal())#
print("The sum of diagonal elements of A is S1",S1)
def cofactor(a):
    def cofactor1(a):
        x=arr[1][1]*arr[2][2]
        y=-(arr[2][1]*arr[1][2])
        return x+y
        print(x,y)
    def cofactor2(a):
        x=arr[0][0]*arr[2][2]
        y=-(arr[2][0]*arr[0][2])
        return x+y
        print(x,y)
    def cofactor3(a):
        x=arr[0][0]*arr[1][1]
        y=-(arr[1][0]*arr[0][1])
        return x+y
        print(x,y)
    return cofactor1(a)+cofactor2(a)+cofactor3(a)
print("The cofactor of the array A is S2=",cofactor(arr))
S2=cofactor(arr)#
M11=arr[0][0]
M12=arr[0][1]
M13=arr[0][2]
M21=arr[1][0]
M22=arr[1][1]
M23=arr[1][2]
M31=arr[2][0]
M32=arr[2][1]
M33=arr[2][2]
print('A=','\t',list([M11,M12,M13]))
print('\t',list([M21,M22,M23]))
print('\t',list([M31,M32,M33]),'\n')
print('|A|=',M11,'*','(',M22,'*',M33,'-',M32,'*',M23,')','-',M12,'*','(',M21,'*',M33,'-',M31,'*',M23,')','+',M13,'*','(',M21,'*',M32,'-',M31,'*',M22,')','\n')
S3=M11*(M22*M33-M32*M23)-M12*(M21*M33-M31*M23)+M13*(M21*M32-M31*M22)
print("THE DETERMINENT OF GIVEN MATRIX IS ABOVE S3"
,S3)
ʎ1=-j;ʎ2=-sol1;ʎ3=-sol2
#S3=round(n.linalg.det(arr))
#print("THE DETERMINENT OF GIVEN MATRIX IS ABOVE S3",S3)
#synthetic division
f=[]
for i in range(1,100):
    f.append(i)
    f.append(-i)
for j in f:
    l=[1,S1,S2,S3]
    ll=[0,0,0,0]
    lll=[1,0,0,0]
    for i in range(1,len(l)):
        ll[i]=(l[i-1]+ll[i-1])*j
        lll[i]=l[i]+ll[i]
    if(lll[-1]==0):
           break
#p=f.index(j)+1
#print(lll,f[p])
#print(lll,j)
#quadratic
a=lll[0]
b=lll[1]
c=lll[2]
d=(b**2)-(4*a*c)   
sol1=int((-b-(math.sqrt(d)))/(2*a))
sol2=int((-b+(math.sqrt(d)))/(2*a))
#print(int(sol1),int(sol2))
print("The values of lamda value ʎ = ",-j,',',-sol1,',',-sol2) 

#(A-ʎI)x=0
x,y,z,ʎ=s.symbols('x y z ʎ')
arri=arr*0
a=arri*ʎ#by multiplying the lamba(ʎ) the a matrixs changed int datatype into object datatype
a[0][0]+=ʎ#so we can assign this operation now because the matrix element is not a int anymore
a[1][1]+=ʎ
a[2][2]+=ʎ
const=n.array([[x,y,z]])
i=(arr-a)*const
Eq1=i[0][0]+i[0][1]+i[0][2]
Eq2=i[1][0]+i[1][1]+i[1][2]
Eq3=i[2][0]+i[2][1]+i[2][2]
eq1=Eq1.subs(ʎ,ʎ1)
eq2=Eq2.subs(ʎ,ʎ1)
sol=solve(eq1,eq2)















