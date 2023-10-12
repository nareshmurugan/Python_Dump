a=input()
arr=list(map(int,input().split()))
arr.sort()
m=2147483648
for i in range(len(arr)-1):
    ab=abs(arr[i]-arr[i+1])
    print(arr[i],'-',arr[i+1],abs(arr[i]-arr[i+1]))
    if ab<m:
        m=ab
        #print(m,ab)
print(m)




    
