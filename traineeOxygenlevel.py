tl=[]
a=0
for i in range(9):
    ol=int(input())
    tl.append(ol)
ch=[x>=100 for x in tl]
if(not False in ch):
    t1ol=round((tl[0]+tl[3]+tl[6])/3)
    t2ol=round((tl[1]+tl[4]+tl[7])/3)
    t3ol=round((tl[2]+tl[5]+tl[8])/3)
    tl=[t1ol,t2ol,t3ol]
    che=[j>70 for j in tl]
    for i in range(3):
        if(che[i]==True):
            if(tl[i]>=max(tl)):
                print('Trainee Number : {}'.format(i+1))
                a+=1
        elif(not True in che):
            print("All trainees are unfit")
            break
else:
    print('INVALID INPUT')
    
