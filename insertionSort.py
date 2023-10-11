def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue=alist[index]
        position=index
    while(position>0 and alist[position-1]>currentvalue):
        alist[position]=alist[position-1]
        position=position-1
    alist[position]=currentvalue
alist=[22,44,11,9]
insertionSort(alist)
print(alist)
