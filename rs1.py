s=input()
n=int(input())
l=len(s)        
if('a' not in s):
    print(0)
if(s=='a'):
    print(0)
'''ss=''
for i in range(n):
    ss+=s
    if(len(ss)>=n):
        break
    #print(ss[0:n].count('a'))
    #print(max([res,ss[0:n].count('a')]))
'''     
f=round(n/l)
c=s.count('a')
res=f*c
#print(ss[0:n].count('a'))
print(res)    
