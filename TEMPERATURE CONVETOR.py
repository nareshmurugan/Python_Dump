d=int(input("ENTER THE DEGREE\t"))
print("FOR FAHRENHEIT PRESS 1 or FOR CELSIUS PRESS 2 AND ENTER")
c=input("ENTER WHAT DO YOU WANT FOR THE DEGREE\t")
if(c=='1'):
    celsius=(d-32)*5/9
    print("THE CELSIUS OF THE DEGREE IS\t",celsius,chr(176),'C')
elif(c=='2'):
    fahrenheit=(d*9/5)+32
    print("THE FAHRENHEIT OF THE DEGREE IS\t",fahrenheit,chr(176),'F')
