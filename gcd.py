a=int(input("Enter the number"))
b=int(input("Enter the number"))
if(b==a):
    return a  
else:
    return gcd(b,a%b)
