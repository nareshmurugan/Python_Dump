a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
if(a[0]>=max(b)+max(c)):
    print(max(b)+max(c))
elif(a[0]>=min(b)+max(c)):
    print(min(b)+max(c))
elif(a[0]>=max(b)+min(c)):
    print(max(b)+min(c))
elif(a[0]>=min(b)+min(c)):
    print(min(b)+min(c))
else:
    print(-1)
    
