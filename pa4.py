odd=set([x*2+1 for x in range(0,5)])
primes=set()
for i in range(2,10):
    j=2
    f=0
    while(j<i):
        if(i%j==0):
            f=1
        j+=1
    if(f==0):
        primes.add(i)
print("odd numbers:",odd)
print("primes numbers:",primes)
print("union:",odd.union(primes))
print("intersection:",odd.intersection(primes))
print("difference:",odd.difference(primes))
print("symmetric differnce:",odd.symmetric_difference(primes))

