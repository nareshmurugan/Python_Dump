s=input()
i=input().split()
strc=list(s)
strc[int(i[0])]=i[1]
result="".join(strc)
print(result)
