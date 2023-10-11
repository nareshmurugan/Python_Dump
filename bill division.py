a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=int(input())
ar=b.pop(a[1])
bt=sum(b)/2
if(bt==c):
    print("Bon Appetit")
else:
    print(int(c-bt))
