ch="yes"
while(ch=="yes"):
    num=int(input("ENTER A NUMBER:\t"))
    if (num==0):
        fact=1
    fact=1
    for i in range (1,num+1):
        fact=fact*i
    print ("FACTORIAL OF",num,"is",fact,'\n')
    ch=input("DO YOU WANT TO SOLVE ANOTHER ONE:\t")
else:
    print("THANKING YOU FOR WORKING")
    
