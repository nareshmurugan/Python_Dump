nl=[]
sl=[]
fuckarr=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    for n in name:
        nl.extend([[name,score]])
    sl.append(score)
sl.sort()
runner=sl[0]
nl=dict(nl)
for i in nl:
    if(nl[i]==runner):
        fuckarr.append(i)
for i in fuckarr:
    print(i)
    
