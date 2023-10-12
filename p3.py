def oddeven(a):
    if (a%2==0):
        return 1
    else:
        return 0
num= int(input("ENTER A NUMBER:"))
if(oddeven(num)==1):
    print("THE GIVEN NUMBER IS EVEN")
elif(oddeven(num)==0):
    print(" THE GIVEN NUMBER IS ODD")
