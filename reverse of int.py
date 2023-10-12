#reverse of a number
a=int(input())
rn=0
while(a>0):
    an=a%10
    rn=(rn*10)+an
    a=int((a-an)/10)
print(rn)
