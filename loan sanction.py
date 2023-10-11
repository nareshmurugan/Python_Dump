dv1=dv2=dv3=dv4=dv5=dv6='yes'
while dv1=='yes':
    account_number=input("ENTER THE ACCOUNT NUMBER");ans=str(account_number)
    if (len(account_number)==4 and int(ans[0])==1):
        account_number=int(account_number)
        dv1='no'
    else:
        dv1='yes'
        print("THE GIVEN ACCOUNT NUMBER IS INVALID")
while dv2=='yes':
    account_balance=int(input("ENTER THE ACCOUNT BALANCE"))
    if (account_balance>=100000):
        dv2='no'
    else:
        dv2='yes'
        print("THE GIVEN ACCOUNT BANK BALANCE WAS INSUFFICENT")
salary=int(input("ENTER THE SALARY AMOUNT"))
loan_type=input("ENTER THE LOAN TYPE")
while dv3=='yes':
    loan_amount_expected=int(input("ENTER THE LOAN AMOUNT EXPECTED"))
    customer_emi_expected=int(input("ENTER THE EMI EXPECTED AMOUNT"))
    if (customer_emi_expected<=loan_amount_expected):
        dv3='no'
    else:
        dv3='yes'
        print("THE GIVEN EMI EXPECTED AMOUNT WAS NOT ELIGIBLE")
print('salary','loan_type','loan_amount_expected','customer_emi_expected')
print(salary,loan_type,loan_amount_expected,customer_emi_expected,sep='          ')

