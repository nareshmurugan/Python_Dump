setlen=int(input())
setele=input().split()
setelem=map(int,setele)
seteleme=set(list(setelem))
setelement=list(list(map(int,setele)))
nooptodo=int(input())
setop=['intersection_update','update','symmetric_difference_update',
        'difference_update']
for i in range(nooptodo):
        opandnoofsetele=input().split()
        setopele=set(input().split())
        for j in range(len(setop)):
            if(opandnoofsetele[i]=='intersection_update'):
                setelement=set(setelement).intersection_update(setopele)
            elif(opandnoofsetele[i]=='update'):
                setelement=set(setelement).update(setopele)
            elif(opandnoofsetele[i]=='symmetric_difference_update'):
                setelement=set(setelement).symmetric_difference_update(setopele)
            elif(opandnoofsetele[i]=='difference_update'):
                setelement=set(setelement).difference_update(setopele)
print(seteleme)
