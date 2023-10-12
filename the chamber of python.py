"""for i in range(int(0b1010)):
    print(int(i),end='\t#')
"""
l=[1,2,3,[1,2],(5,6,7),(2,3,[1,2,3],4,5)]
l.pop(0)
del l[5][0]
print(len(l),l[5][0],l[4][0])

