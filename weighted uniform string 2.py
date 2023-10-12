s=input()
l={}
for i in range(len(s)):
    if i==0 or s[i]!=s[i-1]:
        weight=ord(s[i])-ord('a')+1
        #print(weight)
    else:
        weight+=ord(s[i])-ord('a')+1
        #print(weight)
    l[weight]=1
for i in range(int(input())):
    if(int(input()) in l):
        print("Yes")
    else:
        print("No")
