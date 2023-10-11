a=int(input())
c=input().split()
def jumpingOnClouds(c):
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1: 
        print(1 + jumpingOnClouds(c[1:]))
    if c[2]==0:
        print(1 + jumpingOnClouds(c[2:]))
