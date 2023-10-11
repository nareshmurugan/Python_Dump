fs=input()
nf=int(input())
nfl=[]
for i in range(nf):
    nfs=input()
    nfl.append(nfs)
_f=''
f_=[]
for _i in nfl:
    for __i in _i:
        if(__i in fs):
            _f+='P'
        if(__i not in fs):
            _f+='N'
    f_.append(_f)
    _f=''
for ___i in f_:
    if('P' not in ___i):
        print("POSITIVE")
    else:
        print("NEGATIVE")

    
