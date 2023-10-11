import string as s
l=s.ascii_uppercase
a=input()
p=0
for i in a:
    p+=l.count(i)
print(p+1)
