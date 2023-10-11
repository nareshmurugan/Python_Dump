from collections import Counter as c
n=int(input())
for i in range(n):
    s=input()
    if len(s)%2==1:
        print(-1)
    else:
        ss=c(s[len(s)//2:])-c(s[:len(s)//2])
        print(sum(ss.values()))
