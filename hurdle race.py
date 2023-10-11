a=list(map(int,input().split()))[1]
b=list(map(int,input().split()))
if(max(b)>a):
    print(abs(max(b)-a))
else:
    print(0)
