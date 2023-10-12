def gcd(
    a,b
        ):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    a=int(input("Enter the a "))
    b=int(input("Enter the b "))    
    result=gcd(a,b)
    print(result)
def max_of_list():
    a=[]
    n=int(input("Enter number of elements"))
    for i in range(1,n+1):
        b=int(input("Enter the elements"))
        a.append(b)
    a.sort()
    print("The largest number of the list is :",a[-1])
def linear_search():
    l=[]
    n=int(input("Enter the number of element"))
    s=int(input("Enter the element to search"))
    for i in range(0,n):
        j=int(input("Enter the elements"))
        l.append(j)
    for i in range(0,len(l)):
        if(i==s):
            print("The search number is in position of",i+1)
        
    
def martix_mutiplication():
    
