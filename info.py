def func(A):
    a=list(A)
    a.insert(a.index('='),'=')
    if not eval(''.join(a)):
        co=''
        for i in A[:A.index('=')]:
            co+=i+'+'
        aa=list(co)
        del aa[-1]
        aaa=list('='+A[A.index('='):])
        if(eval(''.join(aa+aaa))):
            print(aa.count('+'))
        else:
            for j in range(aa.count('+')):
                aa.remove('+')
                if(eval(''.join(aa+aaa))):
                    break
            print(aa.count('+'))
    else:
        print(-1)
A=input()
func(A)
