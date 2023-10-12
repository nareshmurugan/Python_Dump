n = "0123456789"
l= "abcdefghijklmnopqrstuvwxyz"
u= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = "!@#$%^&*()-+"
a=int(input())
b=input()
c=0
if a==6 and len(b)!=6:
    print(a-len(b))
elif(a>6):
    for i in b:
        if (i in n):
            c+=1
        elif (i in l):
            c+=1
        elif (i in u):
            c+=1
        elif (i in s):
            c+=1
    print(c)

    
