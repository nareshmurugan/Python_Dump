ch='yes'
while(ch=='yes'):
    p=input("ENTER THE FUNTION TO BE DIFFERENTIATE:\t")
    wrt=input("ENTER THE FUNTION WITH RESPECT TO :\t")
    n=int(input(" ENTER THE POWER OF THE FUNTION:\t"))
    c=int(input("ENTER THE COEFFITIANTE OF X:\t"))
    if(wrt==p):
        print('\n\t','d','/','d',wrt,'=',n,'*',p,'^',n-1,'*','[','d',p,'/','d',wrt,'=',1,']\n\n')
    else:
        print('\n\t','d','/','d',wrt,'=',n*c,'*',p,'^',n-1,'d',p,'/','d',wrt,'\n\n')
    o=input("IF YOU WANT TO FIND F''(X)..........")
    if(o=='yes'):
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
    else:
         print("THANKING YOU FOR FOUND F''(X)")
    o1=input("IF YOU WANT TO FIND F'''(X).........")
    if(o1=='yes'):
        x1=x1*x2
        x2=n-2
        x3=n-3
        if(wrt==p):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','dx','/','dx','=',1,']\n\n')
        else:
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,'\n\n')
    else:
         print("THANKING YOU FOR FOUND F'''(X)")
    o2=input("IF YOU WANT TO FIND F'4(X)..........")
    if(o2=='yes'):
        x1=x1*x2
        x2=n-3
        x3=n-4
        if(wrt==p):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','dx','/','dx','=',1,']\n\n')
        else:
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,'\n\n')
    else:
        print("THANKING YOU FOR FOUND F'4(X)")
    o3=input("IF YOU WANT TO FIND F'5(X)..........")
    if(o3=='yes'):
        x1=x1*x2
        x2=n-4
        x3=n-5
        if(wrt==p):
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'*','[','dx','/','dx','=',1,']\n\n')
        else:
            print('\n\t','d','/','d',wrt,'=',x1*x2,'*',p,'^',x3,'d',p,'/','d',wrt,'\n\n')
    else:
        print("THANKING YOU FOR FOUND F'5(X)")
    ch=input("DO YOU WANT TO FIND THE SOLUTION AGAIN..........")  
else:
 print('THANKING YOU FOR FINDING ALL SOLUTIONS')
