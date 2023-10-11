a=input().split()
m=int(a[0])
n=int(a[1])
for i in range(1,m,2):
    print(((".|.")*(i)).center(n,'-'))
print('WELCOME'.center(n,'-'))
m-=1
for i in range(1,m,2):
    print(((".|.")*(m-i)).center(n,'-'))
    
