def mergeSort(nlist):
    print("Splitting:",nlist)
    if(len(nlist)>1):
        mid=len(nlist)//2
        left_half=nlist[:mid]   
        right_half=nlist[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i=j=k=0
        while(i<len(left_half) and j<len(right_half)):
            if(left_half[i]<right_half[j]):
                nlist[k]=left_half[i]
                i=i+1
            else:
                nlist[k]=right_half[j]
                j=j+1
            k=k+1
        while(i<len(left_half)):
            nlist[k]=left_half[i]
            i=i+1
            k=k+1
        while(j<len(right_half)):
            nlist[k]=right_half[j]
            j=j+1
            k=k+1
        print("Merging:",nlist)
nlist=[14,46,43,27,57,41,45,21,70]
print("\nThe unsorted elements are:",nlist)
mergeSort(nlist)
print("\nThe sorted list is:",nlist)
