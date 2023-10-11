n=int(input())
sm={}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    sm[name] = scores
qn = input()
for i in sm:
    if(i==qn):
        result=sum(sm[i])/len(line)
print("{0:.2f}".format(result))
