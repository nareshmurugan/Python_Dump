a=input().split(':')
nlc=[i for i in range(1,13)]
rlc=[x for x in range(13,25)]
'''
for key in nlc:
    for value in rlc:
        res[key] = value
        rlc.remove(value)
        break
'''
res = {str(nlc[i]):str(rlc[i]) for i in range(len(nlc))}
m=[g for g in range(1,13)]
n=[h for h in range(1,13)]
res1 = {str(m[i]):str(n[i]) for i in range(len(m))}
res['12']='00'
res1['12']='00'
if(a[-1][2:]=='AM'):
    if(len(res1[str(int(a[0]))])!=2):
        print('{}:{}:{}'.format('0'+res1[str(int(a[0]))],a[1],a[-1][:2]))
    else:
        print('{}:{}:{}'.format(res1[str(int(a[0]))],a[1],a[-1][:2]))
elif(a[-1][2:]=='PM'):
    res['12']='12'
    print('{}:{}:{}'.format(res[str(int(a[0]))],a[1],a[-1][:2]))

