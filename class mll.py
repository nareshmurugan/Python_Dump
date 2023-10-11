import numpy as n
#x,Y=int(input("ENTER THE NUMBER OF ROWS")),int(input("ENTER THE NUMBER OF COLUMNS"))
#USING SPLIT FUNCTION WE GET INPUT AS SPACE SPERATED STRING  
a,b,c=str(input("ENTER THE FIRST ROW IN SERIOUS:")),str(input("ENTER THE SECOND ROW IN SERIOUS:")),str(input("ENTER THE THIRD ROW IN SERIOUS"))
print(a,b,c,end='\n')
d,e,f=a.split(),b.split(),c.split()#ASIGNING THE STRING AS ELEMENTS
l=(int(d[0]),int(d[1]),int(d[2]))#R1
k=(int(e[0]),int(e[1]),int(e[2]))#R2
m=(int(f[0]),int(f[1]),int(f[2]))#R3
arr=n.array([l,k,m])#MATRIX(R1,R2,R3)
print("THIS IS THE GIVEN ARRRAY\n",arr)
###############################################################################################
s1=sum(arr.diagonal())
print("The sum of diagonal elements of A is S1",s1)
class cofactor():
    global arr
    a=arr
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
s=cofactor()
print("The cofactor of the array A is S2=",s.cofactor1(a)+s.cofactor2(a)+s.cofactor3(a))

