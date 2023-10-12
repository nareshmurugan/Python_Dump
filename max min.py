import sys
def maxMin(k,arr):
    arr.sort()
    min_diff=sys.maxsize
    for i in range(n-k+1):
        min_diff = min(min_diff,arr[i+k-1]-arr[i])
        return min_diff
n=int(input())
k=int(input())
a=list(set(int(input()) for x in range(n)))
print(maxMin(k,a))
