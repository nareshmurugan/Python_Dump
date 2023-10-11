#a=input()
ch='yes'
#aa=[]
ab=''
while(ch=='yes'):
    a=input()
    if( '@' in a and ".com" in a):
        for i in a:
            #aa.append(i)
            ab+=i
            if(i=='@'):
                break
        if (ab[0:2].isalpha() and ab[-4:-1].isdigit()):
            ch='no'
            a=str(ab)
            break
        else:
            print("""THE EMAIL ID SHOULD BE CONTAIN 3 STRING AND 3 NUMBER\n
                    ENTER THE VALID EMAIL ID AS PER THE CONSTRAINS AGAIN""")
            ch='yes'
        ch='yes'
    else:
        print("THE GIVEN EMAIL ID IS INVALID\nENTER THE VALID EMAIL ID AGAIN")

