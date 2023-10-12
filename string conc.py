from itertools import combinations
a=int(input())
c=0
for i in range(a):
    p=''
    b=input()
    res = [b[x:y] for x, y in combinations(range(len(b) + 1), r = 2)]
    for j in res:
        print(j,p)
        if(j not in p):
            c+=1
            p+=j
    print(*res,c)



