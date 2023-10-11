import string 
a=int(input())
b=input()
c=int(input())
c=c-(26*(c//26))
s1=string.ascii_lowercase
l1=list(s1[c:]+s1[:c])
a1={s1[x]:str(l1[x]) for x in range(len(l1))}
s=''
for i in b:
    if(i.isalpha()):
        if(i.isupper()):
            s+=a1[i.lower()].upper()
        else:
            s+=a1[i]
    else:
        s+=i
print(s)
            
