a=input().split()
b=input().split()
al=list(list(map(int,a)))
bo=list(list(map(int,b)))
ali=0
bob=0
for i in range(len(a)):
    if(al[i]>bo[i]):
        ali+=1
    elif(al[i]<bo[i]):
        bob+=1
print(ali,bob)
            
