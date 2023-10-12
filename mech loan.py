#lex_auth_012693788748742656146

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    #Start writing your code here#lex_auth_012693788748742656146

    if account_number>999 and account_number<=1999:
            if account_balance>=100000:
                if loan_type=="Business" and salary>75000:
                    if customer_emi_expected<=84 and loan_amount_expected<=7500000:
                             eligible_loan_amount=7500000
                             bank_emi_expected=84
                             print("Account number:", account_number)
                             print("The customer can avail the amount of Rs.", eligible_loan_amount)
                             print("Eligible EMIs :", bank_emi_expected)
                             print("Requested loan amount:", loan_amount_expected)
                             print("Requested EMI's:",customer_emi_expected)
                    
                if loan_type=="House" and salary>50000:
                    if customer_emi_expected<=60 and loan_amount_expected<=6000000:
                             eligible_loan_amount=6000000
                             bank_emi_expected=60
                             print("Account number:", account_number)
                             print("The customer can avail the amount of Rs.", eligible_loan_amount)
                             print("Eligible EMIs :", bank_emi_expected)
                             print("Requested loan amount:", loan_amount_expected)
                             print("Requested EMI's:",customer_emi_expected)
                if loan_type=="Car" and salary>25000:
                    if customer_emi_expected<=36 and loan_amount_expected<=500000:
                             eligible_loan_amount=500000
                             bank_emi_expected=36
                             print("Account number:", account_number)
                             print("The customer can avail the amount of Rs.", eligible_loan_amount)
                             print("Eligible EMIs :", bank_emi_expected)
                             print("Requested loan amount:", loan_amount_expected)
                             print("Requested EMI's:",customer_emi_expected)
                    else:
                        "pause"
                else:
                    print("invalid loan type or salary")
            else:
                print("Insufficient account balance")
    else:
        print("invalid account number")
                
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
                     

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1005,90000,255000,"Business",760000,80)
