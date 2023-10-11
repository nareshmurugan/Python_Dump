s=input()
n=int(input())
l=len(s)
if(l==1 and s=='a'):
    print(n)
if('a' not in s):
    print(0)    
if(s[0] and s[-1]!='a'):
    f=round(n/l)
    c=s.count('a')
    res=f*c
    print(res)
elif(len(s)>2 and n>10):
    f=round(n/l)
    c=s.count('a')
    res=f*c
    #print(res)
    ss=''
    for i in range(n):
        ss+=s
        if(len(ss)>=n):
            break
    #print(ss[0:n].count('a'))
    print(max([res,ss[0:n].count('a')]))
    
    
