#uv=uv'+vu'
u=input("ENTER THE U POSITION FUNCTION")
d=input("ENTER THE D POSITION FUNCTION")
if(u=='yes'):
    p=input("ENTER THE FUNTION TO BE DIFFERENTIATE:\t")
    wrt=input("ENTER THE FUNTION WITH RESPECT TO :\t")
    n=int(input(" ENTER THE POWER OF THE FUNTION:\t"))
    c=int(input("ENTER THE COEFFEIENT OF FUNCTION"))
if(d=='yes'):
    p1=input("ENTER THE FUNTION TO BE DIFFERENTIATE:\t")
    wrt1=input("ENTER THE FUNTION WITH RESPECT TO :\t")
    n1=int(input(" ENTER THE POWER OF THE FUNTION:\t"))
    c1=int(input("ENTER THE COEFFEIENT OF FUNCTION"))
    if(wrt==p):
        print('\n\t','d','/','d',wrt,'=',c*n,'*',p,'^',n-1,'*','[','d',p,'/','d',wrt,'=',1,']\n\n')
        p11='\n\t','d','/','d',wrt,'=',c*n,'*',p,'^',n-1,'*','[','d',p,'/','d',wrt,'=',1,']\n\n'
    else:
        print('\n\t','d','/','d',wrt,'=',n*c,'*',p,'^',n-1,'d',p,'/','d',wrt,'\n\n')
        p12='\n\t','d','/','d',wrt,'=',n*c,'*',p,'^',n-1,'d',p,'/','d',wrt,'\n\n'
    if(wrt1==p1):
        print('\n\t','d','/','d',wrt1,'=',c1*n1,'*',p1,'^',n1-1,'*','[','d',p1,'/','d',wrt1,'=',1,']\n\n')
        p21='\n\t','d','/','d',wrt1,'=',c1*n1,'*',p1,'^',n1-1,'*','[','d',p1,'/','d',wrt1,'=',1,']\n\n'
    else:
        print('\n\t','d','/','d',wrt1,'=',n1*c1,'*',p1,'^',n1-1,'d',p1,'/','d',wrt1,'\n\n')
        p22='\n\t','d','/','d',wrt1,'=',n1*c1,'*',p1,'^',n1-1,'d',p1,'/','d',wrt1,'\n\n'
    o=input("IF YOU WANT TO FIND F''(X)..........")
    if(u=='yes'):
        x1=n*c
        x2=n-1
        x3=n-2
        if(wrt==p):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','d',p,'/','d',wrt,'=',1,']\n\n')
        else:
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,'\n\n')
        x1=n*c
        x2=n-1
        x3=n-2
    if(d=='yes'):
        x1=n1*c1
        x2=n1-1
        x3=n1-2
        if(wrt1==p1):
            print('\n\t','d','/','d',wrt1,'=',x1*x2,'*',p1,'^',x3,'*','[','d',p1,'/','d',wrt1,'=',1,']\n\n')
        else:
            print('\n\t','d','/','d',wrt1,'=',x1*x2,'*',p1,'^',x3,'d',p1,'/','d',wrt1,'\n\n')
        x1=n*c
        x2=n-1
        x3=n-2









  
