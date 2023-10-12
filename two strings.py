def twoStrings(a,b):
    if(set(a)-set(b)!=set(a)):
        print(set(a)-set(b),set(a),set(a)-set(b)!=set(a))
        return 'YES'
    else:
        return 'NO'
n=int(input())
for i in range(n):
    print(twoStrings(input(),input()))
    
