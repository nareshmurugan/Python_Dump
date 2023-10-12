def large(s):
    if s>10:return large(s//10)
    else:return s
l1=list(map(int,input().split()));g=[large(j) for j in l1]
print(g)
for k in sorted(set(g)):
    print(f'{k} is  repeated {g.count(k)} times')

