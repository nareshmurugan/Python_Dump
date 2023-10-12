import numpy as n
#x,Y=int(input("ENTER THE NUMBER OF ROWS")),int(input("ENTER THE NUMBER OF COLUMNS"))
#USING SPLIT FUNCTION WE GET INPUT AS SPACE SPERATED STRING
a,b,c=str(input("ENTER THE FIRST ROW IN SERIOUS:")),str(input("ENTER THE SECOND ROW IN SERIOUS:")),str(input("ENTER THE THIRD ROW IN SERIOUS"))
print(a,b,c,end='\n')
d,e,f=a.split(),b.split(),c.split()#ASIGNING THE STRING AS ELEMENTS
l=(d[0],d[1],d[2])#R1
k=(e[0],e[1],e[2])#R2
m=(f[0],f[1],f[2])#R3
g=n.array([l,k,m])#MATRIX(R1,R2,R3)
print("THIS IS THE GIVEN ARRRAY\n",g)
