nl=[]
sl=[]
fuckarr=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    for n in name:
        nl.extend([[name,score]])
    sl.append(score)
sl=set(sl)
sl=list(sl)
sl.sort()
runner=sl[1]
nl=dict(nl)
l=[]
for i_ in nl:
    if(nl[i_]==runner):
        l.append(i_)
l.sort()
for _i in l:
    print(_i)
