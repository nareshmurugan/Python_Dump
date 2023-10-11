a=input()
ab=''
if( '@' in a and ".com" in a):
        for i in a:
            ab+=i
            if(i=='@'):
                break
        if (ab[0:3].isalpha() and ab[-3:-1].isdigit()):
            a=str(ab)
        else:
            print("""THE EMAIL ID SHOULD BE CONTAIN 3 STRING AND 3 NUMBER""")
            a=input()
else:
        print("THE GIVEN EMAIL ID IS INVALID    ")
        a=input()   

