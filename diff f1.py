E=input("ENTER THE EQUATION FOR INPUT COEFFICIENNT IN ONE DIGIT")
e=len(E)
if(e==11 or e==12):
    C=int(E[0])
    p=E[1]
    bp=E[2]
    n=int(E[3])
    ba=E[4]
    C1=int(E[5])
    p1=E[6]
    bp1=E[7] 
    n1=int(E[8])
    bpa1=E[9]
    c=E[10]
    print(C*n,p,bp,n-1,ba,C1*n1,p1,bp1,n1-1)    
else:
    C=int(E[0])
    C1=int(E[1])
    p=E[2]
    bp=E[3]
    n=int(E[4])
    bo=E[5]
    C2=int(E[6])
    C3=int(E[7])
    o=int(E[6:8])
    p1=(E[8])
    bp1=E[9]
    n1=int(E[10])
    bo1=E[11]
    c=E[12]
    o1=int(E[:2])
    print(o1*n,p,bp,n-1,bo,o*n1,p1,bp1,n1-1)


