l=[]
def fibo(n):
    a=0                     
    b=1                      
    while(a<n):           
        a,b=b,a+b
        l.append(a)
i=int(input())
n=fibo(i)
if(l[-2]%2==0):
    print('Alive')
else:
    print('Death')
