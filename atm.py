x=input().split()
a=int(x[0]);b=float(x[1])
if(float(a)>b):
    print(b)
elif(a%5==0):
    print('{:.2f}'.format(float(b-a)-0.50))
else:
    print(b)
