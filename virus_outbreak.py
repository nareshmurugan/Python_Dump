bs=input()
np=int(input())
l=[]
for i in range(np):
    a=input()
    l.append(a)
for i in l:
    for j in range(len(i)):
        ii=0
        if(str(i[j][ii]) in bs):
            print("negative")
        else:
            print("positive")
        ii+=1
                
