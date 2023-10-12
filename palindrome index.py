for i in range(int(input())):
    s=input()
    if(s==s[::-1]):
        print(-1)
    else:
        for j in set(s):
            for k in range(1,s.count(j)+1):
                if(s.replace(j,'',k)==s.replace(j,'',k)[::-1]):
                    print(s.index(j))
                    print(s.replace(j,'',k).index(j))
                print(k,j)
