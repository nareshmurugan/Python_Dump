y=int(input())
c=input()
t=input()
n=input()
input=[y,c,t,n]
cl=["Red", "Green", "Blue", "White", "Black","Grey"]
tl=["Hatchback", "SUV", "MUV", "Sedan"]
dl=["Monday","Tuesday","wednesday","Thursday","Friday","Saturday","Sunday"]
l=[]
if(y%2==0):
    l.append('True')
else:
    l.append('False')
if(y%2!=0):
    l.append('True')
else:
    l.append('False')
if(c in cl[:3]):
    l.append('True')
else:
    l.append('False')
if(c in cl[3:]):
    l.append('True')
else:
    l.append('False')
if(t in tl[:2]):
    l.append('True')
else:
    l.append('False')
if(t in tl[2:]):
    l.append('True')
else:
    l.append('False')
l.append('True')

for i in l:
    print(i)
    
