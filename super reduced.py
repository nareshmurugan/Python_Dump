b=input()
l=[]
for i in range(len(b)):
    if len(l)==0 or l[-1]!=b[i]:
        l.append(b[i])
    else:
        l.pop()
if(len(l)==0):
    print("Empty String")
else:
    print("".join(l))
