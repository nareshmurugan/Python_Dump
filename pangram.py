import string
a=string.ascii_lowercase
s=list(input().lower())
ss=list(set(s))
ss.sort()
sss=ss[1:]
sss=''.join(sss)
if(a==sss or (len(s)==25 and 'x' not in sss)):
    print("pangram")
else:
    print("not pangram")


