a=input()
u=a.split()
m=[]
for y in u:
    m.append(len(y))
q=set(m)
if(len(q)==1):
    h=a.replace(' ','')
    l=[]
    for i in h:
        l.append(ord(i))
    b=''
    for j in range(len(l)):
        if(l[j]==32):
            b+=' '
        else:
            if(j==len(l)-1):
                if(l[-1]>=l[-2]):
                    b+=chr(l[j]).upper()
                    break
                else:
                    b+=chr(l[j]).lower()
                    break
            if(l[j+1]<=l[j]):
                print(l[j+1],l[j])
                if(chr(l[j]).islower()):
                    b+=chr(l[j]).upper()
                else:
                    b+=chr(l[j])
            else:
                b+=chr(l[j])
else:
    for i in u:
        print(i,end=' ')
