import math
def super(l1,j):
    g.append(l1[j])
def encrypt(text,s,x,j):
    if ((s<l)or(x<l)):
        l1=(text[s:x])
        print(l1)
        super(l1,j)
string="hi good morning to all"
text1=string.replace(" ", "")
text=list(text1)
l=len(text)
s=math.sqrt(l)
x=math.floor(s)
y=math.ceil(s)
s=0
m=x
g=[]
for j in range(y):
    g=[]
    for i in range(y):
        encrypt(text,s,x,j)
        s=x
        x=s+m
        print(i,j)
    w="".join(g)
    print(g)
    print(w)
