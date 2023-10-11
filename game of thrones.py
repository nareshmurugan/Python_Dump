from collections import Counter as c
a=input()
total=0
d=c(a)
for i,j in d.items():
    total+=j%2
    print(i,j,total)
if total>1:
    print('NO')
else:
    print('YES')


        
    
