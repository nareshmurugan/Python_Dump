y=int(input("ENTER THE NUMBER OF THE PRIME END"))
odd=set([x*2+1 for x in range(0,y)])
primes=set()
for i in range(2,y):
    while(i==4):
        i+=i
    j=2
    f=0
    while(j<i/2):
        if(i%j==0):
            f=1
        j+=1
    if(f==0):
        primes.add(i)
print(primes)
