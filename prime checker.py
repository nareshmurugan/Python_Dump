a=int(input("Enter the number to check"))
k=0
for i in range(2,a//2):
    if (a%i==0):
        k+=1
if (k<=0):
    print("The given number is prime")

else:
    print("The given number is not a prime")
    
    
