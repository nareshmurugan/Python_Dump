ch='yes'
while(ch=='yes'):
    ch1='yes'
    while(ch1=='yes'):
        if(ch1=='yes'):
            p=p1
            n=n1
            c=c1
        p=input("ENTER THE FUNTION TO BE DIFFERENTIATE:\t")
        n=int(input(" ENTER THE POWER OF THE FUNTION:\t"))
        c=int(input("ENTER THE COEFFITIANTE OF X:\t"))
        wrt=input("ENTER THE FUNTION WITH RESPECT TO :\t")
        ch1=input("DO YOU WANT TO EXPAND THE FUNTION FOR A EQUATION:\t") 
        ch1='yes'
        while(ch1=='yes'):
            ch1=input("DO YOU WANT TO ADD OR SUBRACT ANYTHING ")
            B=input("ENTER THE BINARY OPERATER TO BE USE")
            C=input("ENTER THE CONSTANT VALUE FOR THE EQUATION")
        else:
            print("OK CONTIUNE THE FUNTION TO BE FULL FILL") 
    else:
         print('THANKING YOU FOR FINDING ALL SOLUTIONS')

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
