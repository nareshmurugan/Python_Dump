'''
ch='yes'
while(ch=='yes'):
    if True:
        print('hi')
    ch=input()
else:
    print("bye")
    

account_number=input("ENTER THE ACCOUNT NUMBER");ans=str(account_number)
if (len(account_number)==4 and int(ans[0])==1):
    account_number=int(account_number)
    
else:

dv='yes'
while dv=='yes':
    account_number=input("ENTER THE ACCOUNT NUMBER");ans=str(account_number)
    if (len(account_number)==4 and int(ans[0])==1):
        account_number=int(account_number)
        dv='no'
    else:
        dv='yes'
        print("THE GIVEN ACCOUNT NUMBER IS INVALID")
        
'''
while dv=='yes':
    account_balance=int(input("ENTER THE ACCOUNT BALANCE"))
    if (account_balance>=100000):
        dv='no'
    else:
        dv='yes'
        print("THE GIVEN ACCOUNT BANK BALANCE WAS INSUFFICENT")
        



        
