class Solution:
    def findAnagrams(self, a, b):
        l=len(b)
        an=[]
        u=0
        while 1:
            if(sorted(a[u:l+u])==sorted(b)):
               an.append(u)
            if(u==len(a)):
                break
            u+=1
        return str(an).replace(" ","")
s=Solution()
p=[]
while 1:
    a=input().rstrip('\"').lstrip('\"')
    b=input().rstrip('\"').lstrip('\"')
    p.append([a,b])
    if(
print(s.findAnagrams(a,b))
