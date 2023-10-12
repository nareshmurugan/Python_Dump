l=[]
s=['pear','apple','orange']
for i in s:
    ll=[]
    for j in i:
        a=ord(j)
        ll.append(a)
    l.append(ll)
#lll=[sum(i) for i in l]
#print(s[lll.index(max(lll))])
r=[l[u][0] for u in range(len(l))]
print(s[r.index(max(r))])
