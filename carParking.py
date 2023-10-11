cno=['MH04CC2','MH04C2820','MH04BB3232','MH04CC2113','MH04CC2878',
     'MH04BB8','MH04CC2888','MH04CC1313','MH04CC2222','MH04C1201',
     'MH04CC555','MH04C6565','MH04A7']
op=int(input())
if(op==1):
    cn=input()
    if((6<=len(cn)<=12) and cn.startswith('MH04')):
        cno.append(cn)
    else:
        print("INVALID INPUT") 
elif(op==2):
    cp=input()
    if(cp in cno):
        print("CAR POSITION: {}".format(cno.index(cp)+1))
    else:
        print("INVALID INPUT")
