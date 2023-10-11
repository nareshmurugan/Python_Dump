'''
def mutate_string(s,i,c):
    strc=list(s)
    strc[int(i)]=c
    s_new="".join(strc)
    return s_new
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
'''

'''string = input().strip()
sub_string = input().strip()
si=str(string[0]);sl=len(string)
s=string.count('a',0,5)
print(s) 
'''
'''def l(x,y,z,n):
    l=[[x,y,z] for i in range(n)]
    for i in l:
        print(i)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
a,ae,b,be=input(),input(),input(),input()
ae,be=ae.split(),be.split()
ae=set(map(int,ae))
be=set(map(int,be))
aed=ae-be
bed=be-ae
result=list(aed|bed)
result.sort()
for i in result:
    print(i)
'''
'''
n=int(input())
_n=set(input().split())
b=int(input())
_b=set(input().split())
c=len(_n|_b)
print(c)"""

n=int(input())
_n=set(input().split())
b=int(input())
_b=set(input().split())
c=len(_n&_b)
print(c)


n=int(input())
_n=set(input().split())
b=int(input())
_b=set(input().split())
c=len(_n-_b)
print(c)


n=int(input())
_n=set(input().split())
b=int(input())
_b=set(input().split())
c=len(_n^_b)
print(c)
'''

a=int(input())
_a=set(list(input().split()))
no=int(input())
for i in range(no):
    o_=['intersection_update','update','symmetric_difference_update','difference_update']
    _no=input().split()
    _o=set(list(input().split()))
    for i in range(len(_no)): 
        if(o_[i]=='intersection_update'):
            _a=_a.intersection_update(_o)
        elif(o_[i]=='update'):
             _a.update(_o)
        elif(o_[i]=='symmetric_difference_update'):
            _a=_a.symmetric_difference_update(_o)
        elif(o_[i]=='difference_update'):
            _a=_a.difference_update(_o)
__a=[]
for i in _a:
    __a.append(int(i))
print(sum(__a))    

        
