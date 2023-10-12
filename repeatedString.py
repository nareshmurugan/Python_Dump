s=input()
n=int(input())
if(len(s)==1 and s=='a'):
    print(n)
elif('a' not in s):
    print(0)
else:    
    ss=''
    for i in range(n):
        ss+=s
        if(len(ss)>=n):
            break
    print(ss[0:n].count('a'))
