num1=int(input("ENTER A NUMBER:\t"))
if (num1==0):
    fact=1
fact=1
for i in range (1,num1+1):
    fact=fact*i
print ("FACTORIAL OF",num1,"is",fact)
