import math as m
l=[81,94,11,96,12,35,17,95,28,58]
#l=list(map(int,input().split()))
s=2
print(f'The given list is \n{l}')
while 1:
    k=m.ceil(len(l)/s)
    print(f'\nThe value of k is {k}\n')
    u=k
    for i in range(len(l)):
        if(u==len(l)):
            continue
        print(f'\nThe checking values are {l[i]}<>{l[u]}\n')
        if l[i]>l[u]:
            l[i],l[u]=l[u],l[i]
            print(f'The swapped values are {l[i]}<>{l[u]}\n')

        print(l)     
        u+=1
    s=s*2
    if k==1:
        break
print("\nIn finally we want to perform single time bubble sort\n")
for j in range(len(l)-1):
    if l[j]>l[j+1]:
        l[j],l[j+1]=l[j+1],l[j]
print(f'\nThis is the final swapped list of elements are:\n{l}')
