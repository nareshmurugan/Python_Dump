s=int(input())
a=[1,4,22,33,44,55,66,77,86,97]
l=len(a)-1
mid=round((0+l)/2)
flag=True
while(flag):
    if(s==mid):
        print("element found at",a[mid])
    if(s>mid):
        a=a[:mid]
        l=len(a)-1
        mid=round((0+l)/2)
        if(s==a[mid]):
            flag=False
            print("element found at",a[mid])
    if(s<mid):
        a=a[mid:]
        l=len(a)-1
        mid=round((0+l)/2)
        if(s==a[mid]):
            flag=False
            print("element found at",a[mid])    
