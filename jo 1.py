a=input().split()
b=list(map(int,a))
b.sort()
print(sum(b[:-1]),sum(b[1:]))
