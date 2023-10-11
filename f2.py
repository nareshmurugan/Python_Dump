n=int(input("ENTER THE LIMIT OF SERIES:\t"))
n1=0
n2=1
limit=0
if (n<=0):
    print("please enter the positive integer")
elif(n==1):
    print("fibonacci series for the term 1 is 1")
else:
    print("THE FIBONACCI SERIES WAS")
    for i in range(n):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        i+=1

    
    
