a=' *'
b=10
for i in range(5):
    print(a.center(b,' '))
    a+=a
    b+=2
