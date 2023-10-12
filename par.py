n=int(input())
s='#'*n
c=1
for i in s:
    c-=1
    print(s[:c:])
    
